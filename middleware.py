import jwt
from dotenv import load_dotenv
import os
load_dotenv()
from datetime import datetime

secret_key = os.getenv("secret_key")

def create_token(details,expiry):
    expire =datetime.now() + expiry


    details.update({"exp":expire})

    encoded_jwt = jwt.encode(details, secret_key)

    return encoded_jwt