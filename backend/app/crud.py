from app.models import User
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