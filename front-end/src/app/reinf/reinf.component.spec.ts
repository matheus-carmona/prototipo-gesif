import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReinfComponent } from './reinf.component';

describe('ReinfComponent', () => {
  let component: ReinfComponent;
  let fixture: ComponentFixture<ReinfComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReinfComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReinfComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
