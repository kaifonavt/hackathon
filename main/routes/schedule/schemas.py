from pydantic import BaseModel, Field
from datetime import time

class Schedule(BaseModel):
    id: int
    code: str
    day_of_week: int
    start_time: time
    end_time: time

    class Config:
        from_attributes = True
