from fastapi import HTTPException

from models.user import User
from models.items import Items
from sqlalchemy.orm import Session
from dto import user


def check_user(credentials, db: Session):
    user = db.query(User).filter(User.name == credentials.username).first()

    if user and credentials.password == user.password:
        return user
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


def create_user(data: user.User, db):
    user = User(name=data.name, password=data.password)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user


def get_user(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()


def update_user(db: Session, id: int, new_data: user.User):
    user = db.query(User).filter(User.id == id).first()

    if user:
        for attr, value in new_data.dict().items():
            setattr(user, attr, value)

        db.commit()
        db.refresh(user)
        return user
    return None


def remove(db: Session, id: int):
    user = db.query(User).filter(User.id == id).delete()
    return user


def get_user_with_items(db: Session):
    user_count = db.query(User).count()
    item_count = db.query(Items).count()
    return {
        "user_count": user_count,
        "item_count":item_count

    }