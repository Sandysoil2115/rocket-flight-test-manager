from app.database import SessionLocal
from app.crud import create_user
from app.schemas import UserCreate

db= SessionLocal()
try:
    user = UserCreate(
        name="Sandeep",
        username="sky",
        email="sky@gmail.com",
        password="rocket123"
    )

    created = create_user(db,user)
    print(created.id)
    print(created.username)
finally:
    db.close()