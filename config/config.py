from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables

SQLALCHEMY_DATABASE_URL = os.getenv("Database_URL")
