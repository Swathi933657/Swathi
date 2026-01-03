from fastapi import FastAPI, Request
from supabase import create_client

db_url = "https://suorztdvwvsmsixkkfor.supabase.co"
db_key = "sb_publishable_rl7Ya1ryHSDllAIHzw7_rA_favefr-B"

db = create_client(db_url, db_key)

app = FastAPI()

@app.post('/add/contact')
async def add_contact(request: Request):
    data = await request.json()
    db.table('contacts').insert(data).execute()
    return {"message": "Contact added successfully"}

@app.get('/contacts')
def get_all_contacts():
    result = db.table('contacts').select('*').execute()
    return result.data

@app.get('/contact/{contact_id}')
def get_contact(contact_id: int):
    result = db.table('contacts').select('*').eq('id', contact_id).execute()
    return result.data

@app.put('/contact/{contact_id}')
async def update_contact(request: Request, contact_id):
    data = await request.json()#{'phone':'8765432100}
    result = db.table('contacts').update(data).eq('id', contact_id).execute()
    return "updated successfully"

@app.delete('/contact/{contact_id}')
def delete_contact(contact_id):
    result = db.table('contacts').delete().eq('id', contact_id).execute()
    return "deleted successfully"

