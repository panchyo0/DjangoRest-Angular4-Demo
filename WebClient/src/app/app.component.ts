import { Component,OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Questionnaire} from './questionnaire';
import {FormGroup,FormControl,Validators} from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'Questionnaire Programming Language';
  myform:any;
  questionnaireList:[any];
  levels = ['Junior', 'Middle',
            'Senior', 'Super'];
  model = new Questionnaire('','','','','','','','','','','','');
  maxa=0;

  constructor(private http: HttpClient){

  }
  // OnInit, pull the questionnaire from server not used
  ngOnInit():void {
  this.http.get('http://127.0.0.1:8000/api/questionnaire/?format=json').subscribe(data=>{
    console.log(data);
    this.questionnaireList=data as [any];
    },
    (err:HttpErrorResponse)=>{
      if (err.error instanceof Error){
        console.log("clent-side Error occured");
      }else{
        console.log("server-side Error occured");
      }
    }
  ) ;

  this.myform=new FormGroup({
    Answer_1:new FormControl('',Validators.required),
    Answer_2:new FormControl('',Validators.required),
    Answer_3:new FormControl('',Validators.required),
    Answer_4:new FormControl('',Validators.required),
    Answer_5:new FormControl('',Validators.required),
    Answer_6:new FormControl('',[
      Validators.required,
    ]),
    Answer_7:new FormControl('',Validators.required),
    Answer_8:new FormControl('',Validators.required),
    Answer_9:new FormControl('',Validators.required),
    Answer_10:new FormControl('',[Validators.required]),
    Answer_11:new FormControl('',Validators.required),
    Answer_12:new FormControl('',Validators.required)

  });

  }
  //onSubmit method, submit questionnaire to server
  onSubmit() {
    if (this.myform.valid){
      console.log(this.model);
      const req=this.http.post('http://localhost:8000/api/questionnaire/create/',this.model).subscribe(
          res=>{
            console.log(res);
          },
          err=>{
            console.log("Errot occored");
          }
        )
        window.alert("Submit Success, Thanks!");
        this.myform.reset();
    }else{
      console.log("form not valid");
      window.alert("Form not valid, Please fill all");
    }
  }
  // get diagnostic() { return JSON.stringify(this.model); }

}
