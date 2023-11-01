from fastapi import FastAPI, Depends
import uvicorn
from routers import user as UserRouter
from routers import items as ItemsRouter
from database import SessionLocal, engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(UserRouter.router, prefix='/user')
app.include_router(ItemsRouter.router, prefix='/item')
