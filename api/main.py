from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import Base, engine, SessionLocal
from .models import User
from .auth import hash_pw, verify_pw, create_token, decode_token
from .scan import scan_text

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.post("/signup")
def signup(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, password=hash_pw(password))
    db.add(user)
    db.commit()
    return {"msg": "created"}

@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_pw(password, user.password):
        raise HTTPException(401, "Invalid credentials")
    return {"token": create_token(user.id)}

@app.post("/scan")
def scan(data: str, token: str):
    try:
        decode_token(token)
    except:
        raise HTTPException(401, "Invalid token")

    results = scan_text(data)
    return {"results": results}
