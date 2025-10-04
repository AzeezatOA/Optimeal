import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { GroceriesPage } from './groceries.page';

const routes: Routes = [
  {
    path: '',
    component: GroceriesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes), IonicModule],
  exports: [RouterModule],
})
export class GroceriesPageRoutingModule { }
