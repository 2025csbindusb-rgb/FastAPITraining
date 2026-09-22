from fastapi import FastAPI
app=FastAPI()
@app.get("/")#request to server--get,/-default route
def read_root():
    return {"message": "Hello World","number":44,"is_fun":True}


