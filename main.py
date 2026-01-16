from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI(title="FastAPI Demo")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users",
    summary="Бүх хэрэглэгчдийг шинэээс хуучин руу жагсаах",
    description="Шинэ нь дээрээ бүх хэрэглэгчдийг жагсаана.")
def list_users(db: Session = Depends(get_db)):
    rows = db.execute(text("SELECT id, name FROM users ORDER BY id DESC")).mappings().all()
    return rows