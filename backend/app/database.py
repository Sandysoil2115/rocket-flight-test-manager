#  Mainly contains the connection or representation of database.

# Database url
# Will contain url of database which would be read from the .env file

# Creates a SQLAlchemy engine for the making a base or declarative base so that
# Models.py represent the table

# Session factory : Every request sent the frontend end has its independent session
# so that it can do its task without dependending on other tasks

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine,autocommit=False,autoflush=False)

Base = declarative_base()