from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() #app --> is instance of our FastAPI Object

@app.get("/")
def read_route():
    return {"Message" : "Hello World"}

@app.get("/greet")
def greet():
    return {"Message" : "Hello Sam"}

# Path Parameters
@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None):  #Query Parameter ? Condition
    return {"Message" : f"Hello {name} and you are {age} years old"}
#http://127.0.0.1:8000/greet/Sreeja?age=21

#pydantic  sturcture REquest Body
class Student(BaseModel):
    name: str
    age: int 
    roll: int

#post route
@app.post("/create_student")
def create_student(student: Student):
    return {
        "name" : student.name,
        "age" : student.age,
        "roll" : student.roll
    }


