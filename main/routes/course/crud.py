from sqlalchemy.orm import Session
from typing import Optional
from models import Course

def create_course(db: Session, title: str, instructor_id: int, 
                 duration_weeks: int, total_lessons: int, description: Optional[str] = None):
    db_course = Course(
        title=title,
        instructor_id=instructor_id,
        duration_weeks=duration_weeks,
        total_lessons=total_lessons,
        description=description
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

def update_course(db: Session, course_id: int, title: Optional[str] = None, 
                 description: Optional[str] = None, duration_weeks: Optional[int] = None):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        if title:
            db_course.title = title
        if description is not None:
            db_course.description = description
        if duration_weeks:
            db_course.duration_weeks = duration_weeks
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
        return True
    return False