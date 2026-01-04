from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse
from supabase import create_client

db_url = "https://suorztdvwvsmsixkkfor.supabase.co"
db_key = "sb_publishable_rl7Ya1ryHSDllAIHzw7_rA_favefr-B"


db = create_client(db_url , db_key)

app = FastAPI()

@app.post('/add/student')
async def add_student(request: Request):
    data = await request.json()#{"id":1, "name":"pooja","score":850}
    result = db.table('students').insert(data).execute()
    return "pass"

@app.get('/students')
def get_all_students():
    result = db.table('students').select('*').execute()
    students = result.data
    return students

@app.get('/students/{students_id}')
def get_student(students_id):
    result = db.table('students').select('*').eq('id', students_id).execute()
    data = result.data
    return data

@app.put('/student/{student_id}')
async def update_student(request: Request, student_id):
    data = await request.json()#{'score':900}
    result = db.table('students').update(data).eq('id', student_id).execute()
    return "updated "

@app.delete('/student/{student_id}')
def delete_student(student_id):
    return "deleted "

