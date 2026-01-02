from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse

myapp = FastAPI()


tasks = [
    {
        "id":1,
        "title":"Do Chores",
        "status":"inprogress"
    },
    {
         "id":2,
         "title":"Study Python",
         "status":"inprogress"
    }
]

@myapp.post('/add/task')
async def add_task(request: Request):
    data = await request.json() #{'id':3, 'title':third task', 'status':'incomplete'}
    tasks.append(data)
    return tasks



@myapp.get('/tasks')
def get_all_tasks():
    return tasks

@myapp.get('/task')
def get_task(task_id):
    for t in tasks:
        if t['id'] == int(task_id):
            return t
        
        return "No Such task"
    

@myapp.put('/task')
async def update_task(request: Request):
    data = await request.json()
    for t in tasks:
        if t['id'] == data['id']:
            t.update(data)
            return tasks
        return "No Such task"
    

    @myapp.delete('/task/{task_id}')
    def delete_task(task_id):
        for t in tasks:
            if t['id'] == int(task_id):
                tasks.remove(t)
                return tasks
            return "No such task"