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