import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DfeComponent } from './dfe.component';

describe('DfeComponent', () => {
  let component: DfeComponent;
  let fixture: ComponentFixture<DfeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DfeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DfeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
