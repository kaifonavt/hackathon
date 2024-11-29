from pydantic import BaseModel
from typing import Optional, Dict

class PortfolioBase(BaseModel):
    summary: Optional[str] = None
    skills: Optional[Dict] = None
    achievements_summary: Optional[Dict] = None

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioUpdate(BaseModel):
    summary: Optional[str] = None
    skills: Optional[Dict] = None

class Portfolio(PortfolioBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True