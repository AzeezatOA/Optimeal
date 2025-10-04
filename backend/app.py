import os
import google.generativeai as genai
import requests
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from dotenv import load_dotenv

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
