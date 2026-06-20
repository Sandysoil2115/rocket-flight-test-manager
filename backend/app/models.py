from app.database import Base
from sqlalchemy import Column,Float,Integer,String,Date,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    username = Column(String,unique = True,nullable=False)
    email = Column(String,unique = True,nullable=False)
    password_hash =Column(String,nullable=False)
    flight_tests = relationship("FlightTest",back_populates="owner")

class FlightTest(Base):
    __tablename__ = "flight_tests"
    
    id = Column(Integer,primary_key = True)
    launch_date = Column(Date)
    rocket_name = Column(String,nullable=False)
    rocket_weight = Column(Float)
    launch_angle = Column(Float)
    no_of_motors = Column(Integer)
    thrust = Column(Float)
    status = Column(String)
    reason = Column(String)
    owner_id = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime)
    owner = relationship("User",back_populates="flight_tests")

