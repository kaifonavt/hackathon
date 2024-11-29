from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class ScheduleBase(BaseModel):
    student_id: int
    lesson_id: int
    scheduled_date: datetime
    completion_metadata: Optional[Dict] = None

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(BaseModel):
    scheduled_date: Optional[datetime] = None
    is_completed: Optional[bool] = None
    completion_metadata: Optional[Dict] = None

class Schedule(ScheduleBase):
    id: int
    is_completed: bool

    class Config:
        from_attributes = True