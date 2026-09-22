from fastapi import FastAPI
from pydantic import basemodel
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

pyantic
class Item(Basemodel):
    name:str
    price:float
    in_stock: bool= True

@app.post("/items")
def creat_item(item:Item):
    return {"received":item,"total_price":item.price*1.18}
