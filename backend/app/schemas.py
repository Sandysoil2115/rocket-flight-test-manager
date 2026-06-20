from pydantic import BaseModel,ConfigDict
from datetime import date,datetime

class UserCreate(BaseModel):
    name:str
    username:str
    email:str
    password:str

class UserResponse(BaseModel):
    id: int
    name:str
    username:str
    email:str

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    username:str
    password:str

class FlightTestCreate(BaseModel):
    launch_date: date
    rocket_name: str
    rocket_weight: float
    launch_angle: float
    no_of_motors: int
    thrust: float
    status: str
    reason: str | None = None
    owner_id: int

class FlightTestResponse(BaseModel):
    id: int
    launch_date: date
    rocket_name: str
    rocket_weight: float
    launch_angle: float
    no_of_motors: int
    thrust: float
    status: str
    reason: str | None = None
    owner_id: int
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)
    
class FlightTestUpdate(BaseModel):
    launch_date: date | None = None
    rocket_name: str | None = None
    rocket_weight: float | None = None
    launch_angle: float | None = None
    no_of_motors: int | None = None
    thrust: float | None = None
    status: str | None = None   
    reason: str | None = None