from sqlalchemy.orm import Session
from models.user import User

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.name == username).first()
    if user and user.password == password:
        return user
    return None