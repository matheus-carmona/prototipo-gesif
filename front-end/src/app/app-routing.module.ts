import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DfeComponent } from './dfe/dfe.component';
import { IntegracoesComponent } from './integracoes/integracoes.component';
import { ReinfComponent } from './reinf/reinf.component';
import { HomeScreenComponent } from './screen/home-screen/home-screen.component';
import { SfwComponent } from './sfw/sfw.component';
import { SolfisComponent } from './solfis/solfis.component';

const routes: Routes = [
  {path:'', component: HomeScreenComponent},
  {path:'dfe',component:DfeComponent},
  {path:'solfis',component:SolfisComponent},
  {path:'sfw',component:SfwComponent},
  {path:'reinf',component:ReinfComponent},
  {path:'integracoes',component:IntegracoesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
