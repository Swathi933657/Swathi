from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse

myapp = FastAPI()

balance = [
    {
        "account_id":1,
        "name":"sai",
        "account no":9876543210
       
       
    },
    {
        "account_id":2,
        "name":"munna",
        "account no":8765432109
    }


]

@myapp.post('/add/balance')
async def add_balance(request: Request):
    data = await request.json() #{'account_id':3,'name':'aru','account no':7654321098}
    balance.append(data)
    return balance

@myapp.get('/balance')
async def get_balance():
    return balance

@myapp.get('/balance')
def get_account(account_id):
    for b in balance:
        if b ["account_id"] == int(account_id):
            return b
        return "No such account"
    
@myapp.put('/balance')
async def update_balance(request: Request):
    data = await request.json()
    for b in balance:
        if b ["account_id"] == int(data["account_id"]):
            balance.update(data)
            return balance
        return "No such account"
    
@myapp.delete('/balance/{account_id}')
def delete_balance(account_id):
    for b  in balance:
        if b ["account_id"] == int(account_id):
            balance.remove(b)
            return balance
        return "No such account"
