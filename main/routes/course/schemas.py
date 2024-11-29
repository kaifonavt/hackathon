from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str
    instructor_id: int
    duration_weeks: int
    total_lessons: int
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    duration_weeks: Optional[int] = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True