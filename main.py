from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse

myapp = FastAPI()

#PAYLOAD REQUEST  EXAMPLE
@myapp.post('/save')
async def save_data(request: Request):
    data = await request.json()
    return data


#PATH PARAMETERS EXAMPLE(REQUEST BODY)
@myapp.get('/{name}/details')
def save_data(name):
   return JSONResponse({
          "message": f"Hello {name}"    })




#QUERY PARAMETER EXAMPLE(REQUESTBODY)
@myapp.get('/submit')
def save_data(name, age):
  return JSONResponse({
       "message": f"Hello {name}, your age is {age}"
   })


#JSON RESPONSE EXAMPLE
myapp = FastAPI()
@myapp.get('/JSON')
def  get_JSON():
   data = {
       'name':'sai',
       'age':22
   }
   return JSONResponse(data)







#HTML RESPONSE EXAMPLE
myapp = FastAPI()
@myapp.get('/html')
def  get_html():
   html = '''<!DOCTYPE html>
<html>
<title>HTML Tutorial</title>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

'''

   return HTMLResponse(html)







#REDIRDECT RESPONSE EXAMPLE
myapp = FastAPI()
@myapp.get('/Redirect')
def  get_Redirect():
   url = "https://www.google.com"
   return RedirectResponse(url)