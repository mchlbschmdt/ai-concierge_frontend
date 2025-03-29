from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./properties.db"  # You can replace this with your DB URI

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # For SQLite only
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)
