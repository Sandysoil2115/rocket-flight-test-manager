
class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    username = Column(String,unique = True)
    email = Column(String,unique = True)
    password_hash =Column(String)

class FlightTest(Base):
    __tablename__ = "flight_tests"
    
    id = Column(Integer,primary_key = True)
    Date = Column(Date)
    rocket_name = Column(String)
    rocket_weight = Column(Float)
    launch_angle = Column(Float)
    no_of_motors = Column(Integer)
    thrust = Column(Float)
    status = Column(String)
    reason = Column(String)
    owner_id = Column(Integer,foreign_key = True)
    created_at = Column(DateTime)

