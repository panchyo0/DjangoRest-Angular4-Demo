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
  questionnaireList:[Questionnaire];
  levels = ['Junior', 'Middle',
            'Senior', 'Super'];
  model = new Questionnaire('','','','','','','','','','','','',null);
  maxa=0;

  constructor(private http: HttpClient){

  }
  // OnInit, pull the questionnaire from server not used
  ngOnInit():void {
  this.http.get('http://127.0.0.1:8000/api/questionnaire/?format=json').subscribe(data=>{
    // console.log(data);
    this.questionnaireList=data as [Questionnaire];
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
    Age:new FormControl('',Validators.required),
    Address:new FormControl('',Validators.required),
    C_level:new FormControl('',Validators.required),
    Cpp_level:new FormControl('',Validators.required),
    Do_you_like_open_source_software:new FormControl('',Validators.required),
    Email:new FormControl('',[
      Validators.required,
      Validators.email,
    ]),
    JavaScript_level:new FormControl('',Validators.required),
    Java_level:new FormControl('',Validators.required),
    Name:new FormControl('',Validators.required),
    Phone_Number:new FormControl('',[Validators.required]),
    Python_level:new FormControl('',Validators.required),
    Which_computer_language_are_you_prefer:new FormControl('',Validators.required)

  });

  }
  //onSubmit method, submit questionnaire to server
  onSubmit() {
    if (this.myform.valid){
      // console.log(this.model);
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
