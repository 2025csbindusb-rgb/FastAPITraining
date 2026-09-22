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
@app.get("/student/{rollNo}")
def get_result(rollNo):
    return {"Result":"Distinction","rollNo":rollNo}

#Path parameters with type Hint
@app.get("/candidate/{rollNo}")
def get_candidate(rollNo:int):
    return {"Result":"Distinction","rollNo":rollNo}
