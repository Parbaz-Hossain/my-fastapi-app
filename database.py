from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
#from config.config import SQLALCHEMY_DATABASE_URL
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

# PostgreSQL database URL
## SQLALCHEMY_DATABASE_URL = "postgresql://postgres:post%40%2312%2A%2A@localhost:5432/KnowledgeBaseAIDB"

# Create a new SQLAlchemy engine instance
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Create a new session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the database tables
def create_database():
    Base.metadata.create_all(bind=engine)
