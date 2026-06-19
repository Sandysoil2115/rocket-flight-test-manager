from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name:str
    username:str
    email:str
    password:str

class FlightTestCreate(BaseModel):
    rocket_name: str
    rocket_weight: float
    Date: date
    launch_angle: float
    no_of_motors: int
    thrust: float
    status: str
    reason: str
