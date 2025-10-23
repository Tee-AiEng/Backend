#loat necessary libaries
from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
load_dotenv()
import os

#instantiate yoyr fastapi
app = FastAPI(title="Simple FastAPI", version="1.0.0")
data = [{"name":"Sam Larry","Age":20, "track":"AI Developer"},
        {"name":"Yonda Larry","Age":24, "track":"AI  Enginnering"},
        {"name":"Asa Doe", "Age":19, "track": "Backend Developer"}
        ]

class item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(...,example="Fullstack Developer")


@app.get("/",description="This endpoint returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create data")
def create_data(req:item):
    data.append(req.model_dump())
    print(data)
    return {"Message": "Data Recieved", "Data": data}

@app.put("/update-data/{id}")
def update_data(id: int, req:item):
    data[id] = req.model_dump()
    print(data)
    return {"Message": "Data Recieved", "Data": data}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))

