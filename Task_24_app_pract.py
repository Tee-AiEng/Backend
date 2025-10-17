#import ncessary libaries
from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import uvicorn

#instaciated neccessary libaries
load_dotenv()

app = FastAPI(title="Simple FastAPI", version="1.0.0")
data = [
    {"name":"Kanyisola","Age":25, "track":"AI Engineer"},
    {"name":"Blessing","Age":21, "track":"AI Engineer"},
    {"name":"Ridwan","Age":35, "track":"AI Engineer"},
    {"name":"Tee","Age":23, "track":"AI Engineer"},
    {"name":"David","Age":27, "track":"AI Engineer"}
]

class Enforce(BaseModel):
    name: str = Field(..., min_length=3,max_length=15,example="Divine")
    age: str = Field(...,example=23)
    track: str = Field(...,example="AI Developer")


@app.get("/", description="This endpoint returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI"}


@app.get("/get-data")
def get_data():
    print(data)
    return data


@app.post("/create-data")
def create_data(req:Enforce):
    data.append(req.model_dump())
    print(data)
    return {"Message": "Data Recieved", "Data": data}

@app.put("/change-data/{id}")
def change_data(id:int,req:Enforce):
    data[id] = req.model_dump()
    print(data)
    return {"Message": "Data Changed", "Data": data}

@app.patch("/update-data/{id}")
def update_data(id:int, req:Enforce):
    data[id].update(req.model_dump())
    print(data)
    return {"Message": "Data Updated", "Data": data}
@app.delete("/delete-data")
def delete_data():
    data.clear()
    return {"Message": "Data Deleted", "Data": []}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port_1"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port_1")))