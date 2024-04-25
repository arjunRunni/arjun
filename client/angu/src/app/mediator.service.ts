import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class MediatorService {

  DJANGO_SERVER: string="http://127.0.0.1:8000";

  constructor( private htp:HttpClient) { }


  /////..............addd
  getdata(params:any){
    console.log('......',params)
    return this.htp.post<any>('http://127.0.0.1:8000/create',params)
  }
  public get_all()
  {
    return this.htp.get<any>('http://127.0.0.1:8000/all')
  }

  public get_sing()
  {
    var name="pen"
    return this.htp.get<any>('http://127.0.0.1:8000/all/?name='+name)
  }
}
