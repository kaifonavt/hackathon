from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str
    total_lessons: int
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True