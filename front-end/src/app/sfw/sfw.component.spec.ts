import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SfwComponent } from './sfw.component';

describe('SfwComponent', () => {
  let component: SfwComponent;
  let fixture: ComponentFixture<SfwComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SfwComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SfwComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
