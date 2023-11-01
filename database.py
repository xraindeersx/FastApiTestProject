from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()
SQL_URL="sqlite:///./sql_app.db"
engine=create_engine(SQL_URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()