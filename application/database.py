from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#edited this one this is a bruteforce approach
#docker: postgresql://postgres:password123@172.17.0.3:5432/infoBrent
#normal: postgresql://postgres:password123@localhost/infoBrent

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@localhost:5002/socialMedia"


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