import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';

interface Ingredient {
  name: string;
  price: number;
}

interface Store {
  name: string;
  total: number;
  expanded: boolean;
  breakdown: Ingredient[];
}

@Component({
  selector: 'app-groceries',
  templateUrl: './groceries.page.html',
  styleUrls: ['./groceries.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule]
})

export class GroceriesPage implements OnInit {
  // The highlighted / selected store shown in top card
  selectedStoreTotal = 0;

  // Example stores - totals default to 0 (you can compute these from ingredient lists)
  stores: Store[] = [
    {
      name: 'Costco',
      total: 0,
      expanded: false,
      breakdown: [
        // { name: 'Ingredient A', price: 0.00 },
      ]
    },
    {
      name: `Sam's Club`,
      total: 0,
      expanded: false,
      breakdown: []
    },
    {
      name: 'Target',
      total: 0,
      expanded: false,
      breakdown: []
    },
    {
      name: 'Walmart',
      total: 0,
      expanded: false,
      breakdown: []
    }
  ];

  constructor() { }

  ngOnInit() {
    // You can compute totals here from fetched ingredient lists.
    // For now, keep everything at default zero.
  }

  toggleStore(store: any) {
    store.expanded = !store.expanded;
  }

  viewRecommendations() {
    // click handler intentionally left empty per your request
  }
}
