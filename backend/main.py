from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Person(BaseModel):
    name: str
    surname: str

app = FastAPI()

people_data = [
    {"name": "Thomas", "surname": "Goldman"},
    {"name": "Susie", "surname": "Quattro"},
    {"name": "", "surname": ""}
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get("/people")
def get_people():
    people_data = '''SELECT * FROM db'''
    return people_data

@app.put("/people")
def update_people(people: List[Person]):
    global people_data
    people_data = [person.dict() for person in people]
    return people_data
