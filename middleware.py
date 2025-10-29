import jwt
from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import Request
from datetime import datetime,timedelta
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security

bearer=HTTPBearer()

secret_key = os.getenv("secret_key")

def create_token(details:dict, expiry:int):
    expire = datetime.now() + timedelta(minutes=expiry)


    details.update({"exp":expire})

    encoded_jwt = jwt.encode(details, secret_key)

    return encoded_jwt

def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):

    token= request.credentials

    verified_token = jwt.decode(token, secret_key, algorithms=["HS256"])
   

    return {
        "id": verified_token.get("id"),
        "email":verified_token.get("email"),
        "usertype": verified_token.get("usertype")

    }