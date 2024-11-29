from typing import Dict, Optional
from pydantic import BaseModel

class LessonBase(BaseModel):
    title: str
    content: str
    order: int
    points: int = 0
    lesson_metadata: Optional[Dict] = {}

class LessonCreate(LessonBase):
    course_id: int

class LessonUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    order: Optional[int] = None

class Lesson(LessonBase):
    id: int
    course_id: int

    class Config:
        from_attributes = True