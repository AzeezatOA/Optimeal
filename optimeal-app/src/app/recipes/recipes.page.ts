import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';

@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.page.html',
  styleUrls: ['./recipes.page.scss'],
  imports: [IonicModule]
})
export class RecipesPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
