from app.models import User,FlightTest
from app.auth import hash_password


def create_user(db,user):
    user_db = User(name = user.name,
                   email = user.email,
                   username = user.username,
                   password_hash = hash_password(user.password))
    
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_user_by_username(db,username):
    return db.query(User).filter(User.username == username).first()
def get_user_by_email(db,email):
    return db.query(User).filter(User.email == email).first()
def get_user_by_id(db,user_id):
    return db.query(User).filter(User.id == user_id).first()

# flight Tests

def create_flight_test(db,flight_test):
    flight_test_db = FlightTest(launch_date = flight_test.launch_date,
                                rocket_name = flight_test.rocket_name,
                                rocket_weight = flight_test.rocket_weight, 
                                launch_angle = flight_test.launch_angle,
                                no_of_motors = flight_test.no_of_motors,
                                thrust = flight_test.thrust,
                                status = flight_test.status,
                                reason = flight_test.reason,
                                owner_id = flight_test.owner_id,
    )
    db.add(flight_test_db)
    db.commit()
    db.refresh(flight_test_db)
    return flight_test_db

def get_flight_test_by_id(db,flight_id):
    return db.query(FlightTest).filter(FlightTest.id==flight_id).first()
def get_all_flight_tests(db):
    return db.query(FlightTest).all()
def update_flight_test(flight:FlightTest,flight_db):
    if(flight.launch_date is not None):
        flight_db.launch_date = flight.launch_date
    if(flight.rocket_name is not None):
        flight_db.rocket_name = flight.rocket_name 
    if(flight.rocket_weight is not None):
        flight_db.rocket_weight = flight.rocket_weight
    if(flight.launch_angle is not None):
        flight_db.launch_angle = flight.launch_angle
    if(flight.thrust is not None):
        flight_db.thrust = flight.thrust
    if(flight.no_of_motors is not None):
        flight_db.no_of_motors = flight.no_of_motors
    if(flight.status is not None):
        flight_db.status = flight.status
    if(flight.reason is not None):
        flight_db.reason = flight.reason