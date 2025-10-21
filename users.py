from database_pc import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt

load_dotenv()

app = FastAPI(title="Simple API", version="1.0.0")

class Simple(BaseModel):
    name: str = Field(..., example="Sam Larry")
    email: str = Field(..., example="sam@email.com")
    password: str = Field(..., example="sam123")

@app.post("/signup")
def signup(input: Simple):
    try:
        
        duplicate_query = text(
            """ 
            SELECT * FROM user
            WHERE email = :email
            """
        )
        
        existing = db.execute(duplicate_query, {"email": input.email}).fetchone()
        if existing:
            print("Email already exists")
            # raise HTTPException(status_code=400, detail="Email already exists")
        
        
        query = text("""
            INSERT INTO user (name, email, password)
            VALUES (:name, :email, :password)
                     """)
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode("utf-8"),salt)
        db.execute(query, {"name":input.name, "email":input.email, "password": hashedPassword})
        db.commit()
        
        return {"message": "User created sucessfully",
                "data": {"name":input.name, "email":input.email}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
