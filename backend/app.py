import os
import re
import google.generativeai as genai
import requests
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')
models = genai.list_models()
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from backend! :D'})

@app.route('/ai-suggest', methods=['POST'])
def ai_suggest():
    data = request.json
    prompt = data.get('prompt', 'Given egg and spinach, suggest multiple recipes with ingredients and nutritional values.')
    response = model.generate_content(prompt)
    return jsonify({'suggestion': response.text})

def scout_cheapest_price(product):
    api_key = os.getenv('SERPAPI_API_KEY')
    if not api_key:
        print("Error: SERPAPI_API_KEY not set in .env")
        return None

    params = {
        "engine": "google",                           # Use Google Search engine
        "q": f"buy {product} online",                 # Dynamic query, e.g., "buy eggs online"
        "api_key": api_key       # Load your SerpAPI key from the .env file (keeps it secret)
    }

    try:
        # Create a GoogleSearch object using the defined parameters
        search = GoogleSearch(params)

        # Send the search request and get the results as a Python dictionary (JSON-like)
        results = search.get_dict()
        print(f"SerpApi results for {product}: {results}")
    except Exception as e:
        print(f"Error calling SerpApi: {e}")
        return None

    # Store all extracted data (price, title, URL)
    found_items = []

    # Loop through the organic search results
    for result in results.get("organic_results", []):
        title = result.get("title", "")
        link = result.get("link", "")
        snippet = result.get("snippet", "")

        prices = re.findall(r"\$\d+(?:\.\d{1,2})?", snippet)
        if prices:
            for p in prices:
                print (f"Found price: {p} in snippet: {snippet}")
                try:
                    price_value = float(p.replace("$", ""))   # Convert to float
                    found_items.append({
                        "store": title,       # The title often includes the store name
                        "price": price_value,
                        "url": link
                    })
                except ValueError:
                    continue
    
    print(f"Extracted items: {found_items}")
    # If we found any prices, sort them from cheapest to most expensive
    if found_items:
        found_items.sort(key=lambda x: x["price"])
        cheapest = found_items[0]  # Get the cheapest item
        return cheapest             # e.g., {"store": "Walmart.com", "price": 2.48, "url": "https://..."}
    else:
        return None

@app.route('/scout-price', methods=['POST'])
def scout_price():
    data = request.json
    product = data.get('product')
    if not product:
        return jsonify({'error': 'Product name required'}), 400

    cheapest_price = scout_cheapest_price(product)
    if cheapest_price is not None:
        return jsonify({'product': product, 'cheapest_price': cheapest_price})
    else:
        return jsonify({'error': 'No prices found for the product'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
