import os
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cms.src.infrastructure.logging import logger


POSTGRES_USER = "cms_user"
POSTGRES_PASSWORD = "cms_user_password"
POSTGRES_DB = "cms_database"
POSTGRES_HOST = f"{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}"

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

logger.info("Warming up!")
time.sleep(30)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
