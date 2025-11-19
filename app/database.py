from sqlalchemy import create_engine # for database connection
from sqlalchemy.orm import sessionmaker, declarative_base # for ORM base class
import os # for environment variable access

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/dream_dict_db") # Database connection URL 

# Create the database engine, which is used to interact with the database
engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # base class for ORM models