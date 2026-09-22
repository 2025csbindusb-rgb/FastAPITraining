from fastapi import FastAPI
app=FastAPI()
@app.get("/")#request to server--get,/-default route
def home():
    return {"page":"About","author":"Rakesh"}

@app.get("/health")
def health():
    return {"status":"ok"}

#Post request
@app.post("/create")
def create_something():
    return {"Message":"Created"}

#Path parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}

