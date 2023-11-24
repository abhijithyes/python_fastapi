from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa

# Set the path to the folder containing the .env file
dotenv_path = '/home/neo/neoito/neo/neo/.env'
# Load the environment variables from the .env file
load_dotenv(dotenv_path)
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')


meta = sa.MetaData()

class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)