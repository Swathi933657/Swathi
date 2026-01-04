from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse

app = FastAPI()

persons = [
    {"id": 1, "name": "Ravi", "account_id": 101, "balance": 5000},
    {"id": 2, "name": "Ramya", "account_id": 102, "balance": 3000},
    {"id": 3, "name": "Ramesh", "account_id": 103, "balance": 7000},
]

@app.get("/persons")
def get_all_persons():
    return persons

@app.get("/person/{person_id}")
def get_person(person_id: int):
    for person in persons:
        if person ["id"] == person_id:
            return person
        return "No such person"
    
@app.post("/credit/{account_id}/{amount}")
def credit_amount(account_id: int, amount: int):
    for person in persons:
        if person["account_id"] == account_id:
            person["balance"] += amount
        return "No such account"

@app.post("/debit/{account_id}/{amount}")
def debit_amount(account_id: int, amount: int):
    for person in persons:
        if person ["account_id"] == account_id:
            if person ["balance"] >= amount:
                person ["balance"] -= amount
    return "No such account"




