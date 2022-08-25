from fastapi import FastAPI
from pydantic import BaseModel


# create the app object
app = FastAPI()

db=[]

class Item(BaseModel):
    id: int
    item_name: str
    price: float

# read/index route, opens automatically on  http://127.0.0.1:8000
@app.get("/")
def read():
    return {"greetings":"Welcome"}


@app.get("/items")
def get_items():
    return db


@app.get("/items/{item_id}")
def get_a_item(item_id:int):
    item=item_id-1
    return db[item]

# add item
@app.post("/items")
def add_item(item:Item):
    db.append(item.dict())
    return db[-1]


@app.delete("/item/{item_id}")
def delete_item(item_id:int):
    db.pop(item_id-1)
    return {"task":"deletion successful"}





