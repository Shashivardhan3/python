import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LookuptypeRoutingModule } from './lookuptype-routing.module';
import { LookuptypeComponent } from './lookuptype.component';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { ToastrModule } from 'ngx-toastr';

@NgModule({
  declarations: [LookuptypeComponent],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    LookuptypeRoutingModule,
    NgxDatatableModule,
    ToastrModule.forRoot(),
  ],
})
export class LookuptypeModule {}
