from sqlalchemy.orm import Session
from typing import Optional, Dict
from models import Lesson

def create_lesson(db: Session, course_id: int, title: str, content: str, 
                 order: int, points: int = 0, lesson_metadata: Optional[Dict] = None):
    db_lesson = Lesson(
        course_id=course_id,
        title=title,
        content=content,
        order=order,
        points=points,
        lesson_metadata=lesson_metadata or {}
    )
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def get_lesson(db: Session, lesson_id: int):
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_lessons(db: Session, course_id: Optional[int] = None, skip: int = 0, limit: int = 100):
    query = db.query(Lesson)
    if course_id:
        query = query.filter(Lesson.course_id == course_id)
    return query.offset(skip).limit(limit).all()

def update_lesson(db: Session, lesson_id: int, title: Optional[str] = None, 
                 content: Optional[str] = None, order: Optional[int] = None):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if db_lesson:
        if title:
            db_lesson.title = title
        if content is not None:
            db_lesson.content = content
        if order:
            db_lesson.order = order
        db.commit()
        db.refresh(db_lesson)
    return db_lesson

def delete_lesson(db: Session, lesson_id: int):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if db_lesson:
        db.delete(db_lesson)
        db.commit()
        return True
    return False