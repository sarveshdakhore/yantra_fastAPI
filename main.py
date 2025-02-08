from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal
from db import models
from routes import user
from routes import chat
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(chat.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "FastAPI with SQLite and SQLAlchemy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    