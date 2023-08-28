import { Component, OnInit, ViewChild, TemplateRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DatatableComponent, id } from '@swimlane/ngx-datatable';
import {
  UntypedFormGroup,
  UntypedFormBuilder,
  UntypedFormControl,
  Validators,
} from '@angular/forms';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import Swal from 'sweetalert2';
import { __values } from 'tslib';


@Component({
  selector: 'app-stagedocument',
  templateUrl: './lookuptype.component.html',
  styleUrls: ['./lookuptype.component.sass'],
  providers: [ToastrService],
})
export class LookuptypeComponent implements OnInit {
  shortLink:string = "";
  loading:boolean = false; //Flag variable
  file!:File;
  @ViewChild(DatatableComponent, { static: false }) table: DatatableComponent;
  rows = [];
  scrollBarHorizontal = window.innerWidth < 1200;
  selectedRowData: selectRowInterface;
  newUserImg = 'assets/images/users/user-2.png';
  data = [];
  filteredData = [];
  editForm: UntypedFormGroup;
  register: UntypedFormGroup;
  loadingIndicator = true;
  isRowSelected = false;
  selectedOption: string;
  reorderable = true;
  public selected: any[] = [];
  columns = [
    // { name: 'Document ID' },
    { name: 'lookuptypename' },
    { name: 'shortname' },
    { name: 'parent' },
    { name: 'parentid' },
    { name: 'description' },
    // { name: 'Document Path ' },
    // { name: 'File Name' },
    
    // { name: 'Attachment' },
  ];
  documenttype = [
    { id: '1', value: 'pdf' },
    { id: '2', value: 'xlxs' },
    { id: '3', value: 'txt' },
    { id: '3', value: 'docs' },
  
  ];  

  @ViewChild(DatatableComponent, { static: false }) table2: DatatableComponent;
  apiServer: string;
  httpClient: any;
  dataService: any;
  constructor(

    
    private fb: UntypedFormBuilder,
    private modalService: NgbModal,
    private toastr: ToastrService,
    private http: HttpClient,
    
  )
   {
    this.editForm = this.fb.group({
      // docid: new UntypedFormControl(),
      lookuptypename: new UntypedFormControl(),
      shortname: new UntypedFormControl(),
      parent: new UntypedFormControl(),
      parentid: new UntypedFormControl(),
      description: new UntypedFormControl(),
      // docpath: new UntypedFormControl(),
      // docfname: new UntypedFormControl(),
     
      // attachment: new UntypedFormControl(),
    });
    window.onresize = () => {
      this.scrollBarHorizontal = window.innerWidth < 1200;
    };
  }
  // select record using check box
  onSelect({ selected }) {
    this.selected.splice(0, this.selected.length);
    this.selected.push(...selected);

    if (this.selected.length === 0) {
      this.isRowSelected = false;
    } else {
      this.isRowSelected = true;
    }
  }
  deleteSelected() {
    Swal.fire({
      title: 'Are you sure?',
      showCancelButton: true,
      confirmButtonColor: '#8963ff',
      cancelButtonColor: '#fb7823',
      confirmButtonText: 'Yes',
    }).then((result) => {
      if (result.value) {
        this.selected.forEach((row) => {
          this.deleteRecord(row);
        });
        this.deleteRecordSuccess(this.selected.length);
        this.selected = [];
        this.isRowSelected = false;
      }
    });
  }
  ngOnInit() {
    this.fetch((data) => {
      this.data = data;
      this.filteredData = data;
      setTimeout(() => {
        this.loadingIndicator = false;
      }, 500);
    });
    this.register = this.fb.group({
      id:  [''],
      img:  [''],
      // docid:  ['', [Validators.required]],
      lookuptypename:  ['', [Validators.required]],
      shortname:  ['', [Validators.required]],
      parent:  ['', [Validators.required]],
      parentid:  ['', [Validators.required]],
      description: ['', [Validators.required]],
      // docpath: ['', [Validators.required]],
      // docfname: ['', [Validators.required]],
      
      // attachment:  ['', [Validators.required]],

    });


    
  }
  // fetch data
  fetch(cb) {
    const req = new XMLHttpRequest();
    req.open('GET', 'http://59.90.29.10:44444/api/lookuptypes');
    req.onload = () => {
      const data = JSON.parse(req.response);
      cb(data);
    };
    req.send();
  }
  
  // add new record
  addRow(content) {
    this.modalService.open(content, {
      ariaLabelledBy: 'modal-basic-title',
      size: 'lg',
    });
    this.register.patchValue({
      id: this.getId(10, 100),
      img: this.newUserImg,
    });
  }
  // edit record
  editRow(row, rowIndex, content) {
    this.modalService.open(content, {
      ariaLabelledBy: 'modal-basic-title',
      size: 'lg',
    });
    this.editForm.setValue({
      // id: row.id,
      // img: row.img,
      // docid: row.docid,
      lookuptypename: row.lookuptypename,
      shortname: row.shortname,
      parent: row.parent,
      parentid: row.parentid,
      description: row.description,
      // objtype:  row.objtype,
      // documenttype2: row.documenttype2,
      // docpath: row.docpath,
      // docfname: row.docfname,
      
      // attachment: row.attachment,
      // createdby: row.createdby,
      // modifiedby: row.modifiedby,
    });
    this.selectedRowData = row;
  }
  // delete single row
  // deleteSingleRow(row) {
  //   Swal.fire({
  //     title: 'Are you sure?',
  //     showCancelButton: true,
  //     confirmButtonColor: '#8963ff',
  //     cancelButtonColor: '#fb7823',
  //     confirmButtonText: 'Yes',
  //   }).then((result) => {
  //     if (result.value) {
  //       this.deleteRecord(row);
  //       this.deleteRecordSuccess(1);
  //     }
  //   });
  // }

  deleteSingleRow(row) {
    Swal.fire({
      title: 'Are you sure?',
      showCancelButton: true,
      confirmButtonColor: '#8963ff',
      cancelButtonColor: '#fb7823',
      confirmButtonText: 'Yes',
    }).then((result) => {
      if (result.value) {
        this.deleteRecord(row);
        this.deleteRecordSuccess(1);
      }
    });
  }

  deleteRecord(row) {
    this.data = this.data.filter(r => r !== row);
      this.http.delete(`http://59.90.29.10:44444/api/lookuptypes/parent/DocumentType/${row.lookuptypename}`).subscribe(() => {
        this.data = this.data.filter(r => r !== row);
    });
  }

  getdata() {
    throw new Error('Method not implemented.');

  }
  arrayRemove(array, id) {
    return array.filter(function (element) {
      return element.id !== id;
    });
  }
  // save add new record
  onAddRowSave(form: UntypedFormGroup) {
    // this.data.push(form.value);
    // this.data = [...this.data];
    // form.reset();
    // this.modalService.dismissAll();
    // this.addRecordSuccess();
    this.http.post('http://59.90.29.10:44444/api/lookuptypes/parent/DocumentType', form.value).subscribe(() => {
      // Successfully saved data
      this.data.push(form.value);
      this.data = [...this.data];
      form.reset();
      this.modalService.dismissAll();
      this.addRecordSuccess();
    }, (error) => {
      // Handle error saving data
      console.error(error);
    });
  }

  httpOptions<T>(arg0: string, arg1: string, httpOptions: any) {
    throw new Error('Method not implemented.');
  }
  // save record on edit
  onEditSave(form: UntypedFormGroup) {
    const record = form.value;
    this.http.put(`http://59.90.29.10:44444/api/lookuptypes/parent/DocumentType/${record.lookuptypename}`, record).subscribe(() => {
      this.data = this.data.map((value) => {
        if (value.lookuptypename == record.lookuptypename) {
          return record;
        }
        return value;
      });
      const index = this.data.findIndex((value) => value.docid == record.docid);
      this.data[index] = record;
      this.editRecordSuccess();
      this.modalService.dismissAll();
    }, (error) => {
      // Handle error updating data
      console.error(error);
      this.editRecordSuccess();
      this.modalService.dismissAll();  
    });
  }  
    // this.data = this.data.filter((value, key) => {
    //   if (value.id == form.value.id) {
    //     value.docid = form.value.docid;
    //     value.docname = form.value.docname;
    //     value.doctype = form.value.doctype;
    //     value.objid = form.value.objid;
    //     value.objname = form.value.objname;
    //     value.objtype = form.value.objtype;
    //     // value.documenttype2 = form.value.documenttype2;
    //     value.docpath = form.value.docpath;
    //     value.docfname = form.value.docfname;
    //     value.filefrmt = form.value.filefrmt;
    //     value.attachment = form.value.attachment;
    //     // value.createdby= form.value.createdby;
    //     // value.modifiedby= form.value.modifiedby;
    //   }
    //   this.modalService.dismissAll();
    //   return true;
    // });
    // this.editRecordSuccess();
  
  // filter table data
  filterDatatable(event) {
    // get the value of the key pressed and make it lowercase
    const val = event.target.value.toLowerCase();
    // get the amount of columns in the table
    const colsAmt = this.columns.length;
    // get the key names of each column in the dataset
    const keys = Object.keys(this.filteredData[0]);
    // assign filtered matches to the active datatable
    this.data = this.filteredData.filter(function (item) {
      // iterate through each row's column data
      for (let i = 0; i < colsAmt; i++) {
        // check for a match
        if (
          item[keys[i]].toString().toLowerCase().indexOf(val) !== -1 ||
          !val
        ) {
          // found match, return true to add to result set
          return true;
        }
      }
    });
    // whenever the filter changes, always go back to the first page
    this.table.offset = 0;
  }
  // get random id
  getId(min: number , max: number) {
    // min and max included
    return Math.floor(Math.random() * (max - min + 1) + min);
  }
  addRecordSuccess() {
    this.toastr.success('Add Record Successfully', '');
  }
  editRecordSuccess() {
    this.toastr.success('Edit Record Successfully', '');
  }
  deleteRecordSuccess(count) {
    this.toastr.error(count + ' Records Deleted Successfully', '');
  }
}
export interface selectRowInterface {
  // img: String;
  firstName: String;
  // lastName: String;
}

