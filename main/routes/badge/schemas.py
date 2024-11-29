from typing import Dict, Optional
from pydantic import BaseModel

class BadgeBase(BaseModel):
    name: str
    number: int
    description: Optional[str] = None
    styles: Optional[Dict] = None
    requirements: Optional[Dict] = None

class BadgeCreate(BadgeBase):
    pass

class BadgeUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    styles: Optional[Dict] = None

class Badge(BadgeBase):
    id: int

    class Config:
        from_attributes = True