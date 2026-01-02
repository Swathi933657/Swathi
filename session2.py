from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse

myapp = FastAPI()

contacts = [
    {
        'id':1,
        'name':'John',
        'phone':'9876543210'
    },
    {
        'id':2,
        'name':'sai',
        'phone':'9865743210'
    }
]

@myapp.post('/add/contacts')
async def add_contact(request: Request):
    data = await request.json()#{'id':3,'name':munna,'phone':'88967543218'}
    contacts.append(data)
    return contacts


@myapp.get('/contacts')
def get_all_contacts():
    return contacts

@myapp.get('/contact')
def get_contact(contact_id):
    for c in contacts:
        if c['id'] == int(contact_id):
            return c
        return "No such contact"
    

@myapp.put('/contact')
async def update_contact(request: Request):
    data = await request.json()
    for c in contacts:
        if c['id'] == data['id']:
            c.update(data)
            return contacts
        return "No such contact"
    

@myapp.delete('/contact/{contact_id}')
def delete_contact(contact_id):
    for c in contacts:
        if c ['id'] == int(contact_id):
            contacts.remove(c)
            return contacts
        return "No such contact"