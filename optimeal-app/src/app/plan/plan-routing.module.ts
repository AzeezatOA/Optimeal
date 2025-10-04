import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { PlanPage } from './plan.page';

const routes: Routes = [
  {
    path: '',
    component: PlanPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule, IonicModule],
})
export class PlanPageRoutingModule { }
