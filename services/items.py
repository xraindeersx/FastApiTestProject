from models.items import Items
from sqlalchemy.orm import Session
from dto.item import Item as ItemDTO


def create_item(data: ItemDTO, user_id: int, db: Session):

    item = Items(name=data.name,user_id=user_id)
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
    except Exception as e:
        print(e)
    return item


def get_item(db: Session):
    return db.query(Items).all()


def update_item(data: ItemDTO, db: Session, id: int):
    item = db.query(Items).filter(Items.id == id).first()
    item.name = data.name
    item.user_id=data.user_id
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def remove_item(db: Session, id: int):
    item = db.query(Items).filter(Items.id == id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False