from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    role: str
    active: bool = True

class Record(BaseModel):
    id: Optional[int] = None
    amount: float
    type: str
    category: str
    date: str
    note: str