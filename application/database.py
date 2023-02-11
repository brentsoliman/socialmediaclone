from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#edited this one this is a bruteforce approach
#docker: postgresql://postgres:password123@172.17.0.3:5432/infoBrent
#normal: postgresql://postgres:password123@localhost/infoBrent

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}' 


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Dependency for making a session 
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()