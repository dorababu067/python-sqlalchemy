from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


# Retrieve database URL from environment variables
DATABASE_URL = config("DATABASE_URL")

# Create a SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# Bind the scoped session to the engine
# Create a session factory with a scoped session for thread safety
db = scoped_session(sessionmaker(bind=engine))

# initialize declarative base class
Base = declarative_base()
