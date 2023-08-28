import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LookuptypeComponent } from './lookuptype.component';

const routes: Routes = [
  {
    path: '',
    component: LookuptypeComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LookuptypeRoutingModule {}