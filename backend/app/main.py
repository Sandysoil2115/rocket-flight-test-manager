from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate,UserResponse,UserLogin,FlightTestCreate,FlightTestResponse,FlightTestUpdate
from app.crud import create_user,get_user_by_email,get_user_by_username,create_flight_test,get_all_flight_tests,get_flight_test_by_id,update_flight_test
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


@app.post("/flight-tests",response_model=FlightTestResponse)
def register_flight_Test(flight_test:FlightTestCreate,db:Session=Depends(get_db)):
    return create_flight_test(db,flight_test)

@app.get("/flight-tests",response_model=list[FlightTestResponse])
def flights(db:Session=Depends(get_db)):
    return get_all_flight_tests(db)

@app.get("/flight-tests/{id}",response_model=FlightTestResponse)
def getflight(id:int ,db: Session=Depends(get_db)):
    flight_db = get_flight_test_by_id(db,id)
    if flight_db is None:
        raise HTTPException(status_code=404,detail="Flight test not found")
    return flight_db

@app.put("/flight-tests/{id}",response_model=FlightTestResponse)
def update(id:int , flight: FlightTestUpdate, db: Session=Depends(get_db)):
    flight_db = get_flight_test_by_id(db,id)
    if flight_db is None:
        raise HTTPException(status_code=404,detail="Flight test not found")
    update_flight_test(flight,flight_db)
    db.commit()
    return flight_db

@app.delete("/flight-tests/{id}")
def remove(id:int , db: Session=Depends(get_db)):
    flight_db = get_flight_test_by_id(db,id)
    if flight_db is None:
        raise HTTPException(status_code=404,detail="Flight test not found")
    db.delete(flight_db)
    db.commit()
    return {"message":"Deleted the flight test successfully"}