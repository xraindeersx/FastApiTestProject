from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import items as ItemService
from dto.item import Item as ItemDTO
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from services.user import check_user
from typing import Annotated

router = APIRouter()
security = HTTPBasic()

@router.post('/', tags=['item'])
async def create(credentials: Annotated[HTTPBasicCredentials, Depends(security)],data: ItemDTO = None, owner_id: int = None, db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return ItemService.create_item(data, owner_id, db)
    else:
        user


@router.get('/all_items', tags=['item'])
async def get(credentials: Annotated[HTTPBasicCredentials, Depends(security)],db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return ItemService.get_item(db)
    else:
        user


@router.put("/{id}", tags=["item"])
async def put(credentials: Annotated[HTTPBasicCredentials, Depends(security)],id: int = None, data: ItemDTO = None, db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return ItemService.update_item(data, db, id)
    else:
        user


@router.delete('/{id}', tags=['item'])
async def delete(credentials: Annotated[HTTPBasicCredentials, Depends(security)],id: int = None, db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return ItemService.remove_item(db, id)
    else:
        user