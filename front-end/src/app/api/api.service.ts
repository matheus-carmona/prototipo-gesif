import { Injectable } from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  constructor(private http: HttpClient) { }
  getTeste():Observable<any>{
    return this.http.get<any>("http://127.0.0.1:5000/teste")
  }
}
