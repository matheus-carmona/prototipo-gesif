import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api/api.service';

@Component({
  selector: 'app-home-screen',
  templateUrl: './home-screen.component.html',
  styleUrls: ['./home-screen.component.css']
})
export class HomeScreenComponent implements OnInit {

  constructor(private api : ApiService) { }
  teste = ''
  ngOnInit(): void {
    this.api.getTeste().subscribe(data => {
      console.log(data)
      this.teste = data
    })
  }

}
