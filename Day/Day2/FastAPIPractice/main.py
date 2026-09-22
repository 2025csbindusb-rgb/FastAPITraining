from fastapi import FastAPI
app=FastAPI()
@app.get("/")#request to server--get,/-default route
def home():
    return {"page":"About","author":"Rakesh"}

@app.get("/health")
def health():
    return {"status":"ok"}


