from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate,UserResponse,UserLogin
from app.crud import create_user,get_user_by_email,get_user_by_username
from app.dependencies import get_db
from app.auth import verify_password

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome"}

@app.get("/health")
def health():
    return {"status":"running"}

@app.post("/register",response_model=UserResponse)
def register(user:UserCreate,db: Session=Depends(get_db)):
    if(get_user_by_username(db,user.username)):
        raise HTTPException(status_code=409,detail="Username already exists")
    if(get_user_by_email(db,user.email)):
        raise HTTPException(status_code=409,detail="Email already exists")    
    return create_user(db,user)
    
@app.post("/login")
def login(user:UserLogin,db: Session=Depends(get_db)):
    db_user = get_user_by_username(db,user.username)
    if(db_user is None):
        raise HTTPException(status_code=401,detail="Invalid Username or Password")
    if not (verify_password(user.password,db_user.password_hash)):
        raise HTTPException(status_code=401,detail="Invalid Username or Password")
    return {"message":"success"}
