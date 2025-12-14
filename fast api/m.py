from fastapi import FastAPI

app=FastAPI()

@app.get('/') #used to define a path in fast api 

# its an app decorater and it defines a path for the HTTP GET method and path is / which is root directory
