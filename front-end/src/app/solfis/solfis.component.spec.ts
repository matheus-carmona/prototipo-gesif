import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SolfisComponent } from './solfis.component';

describe('SolfisComponent', () => {
  let component: SolfisComponent;
  let fixture: ComponentFixture<SolfisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SolfisComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SolfisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
