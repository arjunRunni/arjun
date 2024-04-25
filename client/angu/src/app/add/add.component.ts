import { Component } from '@angular/core';
import { MediatorService } from '../mediator.service';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent {

  constructor(private mService:MediatorService){}

  ///.....
  add(data:any){
    console.log('mydata',data)
    
  }

}
