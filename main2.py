from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse
from supabase  import create_client



db_url = "https://suorztdvwvsmsixkkfor.supabase.co"
db_key = "sb_publishable_rl7Ya1ryHSDllAIHzw7_rA_favefr-B"


db = create_client(db_url, db_key)


app = FastAPI()




@app.post('/add/task')
async def add_task(request: Request):
    data = await request.json()#{"id":2, "title":"second task","status":"pending"}
    # print(data)
    result = db.table('tasks').insert(data).execute()
    return "success"

@app.get('/tasks')
def get_all_tasks():
    result = db.table('tasks').select('*').execute()
    tasks = result.data
    return tasks


@app.get('/task')
def get_task(task_id):
    result  = db.table('tasks').select('*').eq('id', task_id).execute()
    data = result.data
    return data
        
       
    

@app.put('/task/{task_id}')
async def update_task(request: Request, task_id):
    data = await request.json()#{ 'status':'done'}
    result = db.table('tasks').update(data).eq('id', task_id).execute()
    return "Updated successfully"
    
@app.delete('/task/{task_id}')
def delete_task(task_id):
        result = db.table('tasks').delete().eq('id', task_id).execute()
        return "Deleted successfully"
        
        