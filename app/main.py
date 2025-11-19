from fastapi import FastAPI, Request, HTTPException, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.hash import bcrypt
from jose import jwt
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import Session # for database session management
from database import SessionLocal, engine, Base
import schemas, models, database

#Base.metadata.create_all(bind=engine)
app = FastAPI()  
SECRET = "117909" # secret key for JWT, which is used for encoding and decoding tokens

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Temporary "in-memory" storage (later replaced with DB)
symbols = []

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/analyze_dream/")
def analyze_dream(dream: schemas.DreamCreate):
    import openai
    client = OpenAI()

    return {"message": "User created!"}
    #response = openai.ChatCompletion.create(
    #    model="gpt-4",
    #    messages=[{"role": "user", "content": dream.content}]
    #)
    #return {"interpretation": response['choices'][0]['message']['content']}


@app.post("/symbols/")
def create_symbol(symbol: schemas.SymbolCreate, db: Session = Depends(get_db)):
    db_symbol = models.Symbol(**symbol.dict(), user_id=1)  # temporary user_id
    db.add(db_symbol)
    db.commit()
    db.refresh(db_symbol)
    return db_symbol

# When the root is loaded, return a welcome message
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "symbols": symbols})


@app.post("/add-symbol")
def add_symbol(symbol: str = Form(...), meaning: str = Form(...)):
   symbols.append({"symbol": symbol, "meaning": meaning})
   return RedirectResponse("/", status_code=303)

# When the /register endpoint is called, register a new user
@app.post("/register") # Endpoint for user registration
def register(user: dict):
    hashed = bcrypt.hash(user["password"])
    # store user["name"], user["email"], hashed in DB
    return RedirectResponse("/", status_code=303)

# When the /login endpoint is called, authenticate the user and return a JWT token
@app.post("/login")
def login(user: dict):
    # fetch user from DB
    if not user_db:
        raise HTTPException(status_code=400, detail="User not found")
    if not bcrypt.verify(user["password"], user_db["password_hash"]):
        raise HTTPException(status_code=400, detail="Invalid password")
    token = jwt.encode({"user_id": user_db["id"]}, SECRET, algorithm="HS256")
    return {"token": token}
