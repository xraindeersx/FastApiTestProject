from pydantic import BaseModel
from datetime import datetime
class Item(BaseModel):
    name:str
    user_id:int
    created_at:datetime
    updated_at:datetime