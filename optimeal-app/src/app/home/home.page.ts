import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  imports: [IonicModule, FormsModule, CommonModule],
  standalone: true
})
export class HomePage {
  mealInput: string = '';
  meals: string[] = [];
  constructor(private router: Router) { }

  addMeal() {
    const meal = this.mealInput.trim();
    if (meal) {
      this.meals.push(meal);
      this.mealInput = '';
    }
  }

  removeMeal(index: number) {
    // remove the meal at the provided index if valid
    if (index >= 0 && index < this.meals.length) {
      this.meals.splice(index, 1);
    }
  }

  generateRecipes() {
    // navigate to the recipes page
    this.router.navigate(['/recipes']);
  }
}
