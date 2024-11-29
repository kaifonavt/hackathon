from pydantic import BaseModel
from datetime import date
from typing import Optional, Dict

class PersonalGoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    target_date: date
    progress_data: Optional[Dict] = None

class PersonalGoalCreate(PersonalGoalBase):
    pass

class PersonalGoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class PersonalGoal(PersonalGoalBase):
    id: int
    user_id: int
    status: Optional[str] = None

    class Config:
        orm_mode = True