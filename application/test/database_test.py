from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..database import Base





#edited this one this is a bruteforce approach
#docker: postgresql://postgres:password123@172.17.0.3:5432/infoBrent
#normal: postgresql://postgres:password123@localhost/infoBrent

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5003/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()