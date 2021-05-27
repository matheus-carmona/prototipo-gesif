import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { HomeScreenComponent } from './screen/home-screen/home-screen.component';
import { DfeComponent } from './dfe/dfe.component';
import { SolfisComponent } from './solfis/solfis.component';
import { SfwComponent } from './sfw/sfw.component';
import { ReinfComponent } from './reinf/reinf.component';
import { IntegracoesComponent } from './integracoes/integracoes.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeScreenComponent,
    DfeComponent,
    SolfisComponent,
    SfwComponent,
    ReinfComponent,
    IntegracoesComponent,
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
