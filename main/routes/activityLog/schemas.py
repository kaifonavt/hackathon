from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class ActivityLogBase(BaseModel):
    activity_type: str
    description: Optional[str] = None
    points_earned: int = 0
    activity_log_metadata: Optional[Dict] = None

class ActivityLogCreate(ActivityLogBase):
    user_id: int

class ActivityLogUpdate(BaseModel):
    description: Optional[str] = None
    points_earned: Optional[int] = None
    activity_log_metadata: Optional[Dict] = None

class ActivityLog(ActivityLogBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True