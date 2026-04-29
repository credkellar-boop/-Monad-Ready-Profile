import jwt, datetime, os
from passlib.hash import bcrypt

SECRET = os.getenv("JWT_SECRET", "devsecret")

def hash_pw(pw):
    return bcrypt.hash(pw)

def verify_pw(pw, h):
    return bcrypt.verify(pw, h)

def create_token(user_id):
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
