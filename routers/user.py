from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService
from dto import user as UserDTO
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from services.user import check_user
from services.user import get_user_with_items

router = APIRouter()
security = HTTPBasic()


@router.get("/count", tags=["check"])
def count_user_and_item(credentials: Annotated[HTTPBasicCredentials, Depends(security)],db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return get_user_with_items(db)
    else:
        user


@router.post('/', tags=['user'])
async def create(data: UserDTO.User = None, db: Session = Depends(get_db), ):
    return UserService.create_user(data, db)


@router.get('/{id}', tags=['user'])
async def get(credentials: Annotated[HTTPBasicCredentials, Depends(security)],id: int = None,db: Session = Depends(get_db), ):
    user=check_user(credentials, db)
    if user:
        return UserService.get_user(id, db)
    else:
        return user


@router.put("/{id}", tags=["user"])
async def put(credentials: Annotated[HTTPBasicCredentials, Depends(security)],id: int = None, data: UserDTO.User = None, db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return UserService.update(data, db, id)
    else:
        return user

@router.delete('/{id}', tags=['user'])
async def delete(credentials: Annotated[HTTPBasicCredentials, Depends(security)],id: int = None, db: Session = Depends(get_db)):
    user = check_user(credentials, db)
    if user:
        return UserService.remove(db, id)
    else:
        return user