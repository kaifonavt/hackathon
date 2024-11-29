# crud/schedule.py
from sqlalchemy.orm import Session
from typing import Optional, Dict
from datetime import datetime
from models import Schedule

def create_schedule(db: Session, student_id: int, lesson_id: int, 
                   scheduled_date: datetime, completion_metadata: Optional[Dict] = None):
    db_schedule = Schedule(
        student_id=student_id,
        lesson_id=lesson_id,
        scheduled_date=scheduled_date,
        completion_metadata=completion_metadata or {}
    )
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def get_schedule(db: Session, schedule_id: int):
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()

def get_student_schedules(db: Session, student_id: int, skip: int = 0, limit: int = 100):
    return db.query(Schedule)\
        .filter(Schedule.student_id == student_id)\
        .order_by(Schedule.scheduled_date)\
        .offset(skip).limit(limit).all()

def get_lesson_schedules(db: Session, lesson_id: int, skip: int = 0, limit: int = 100):
    return db.query(Schedule)\
        .filter(Schedule.lesson_id == lesson_id)\
        .order_by(Schedule.scheduled_date)\
        .offset(skip).limit(limit).all()

def update_schedule(db: Session, schedule_id: int, 
                   scheduled_date: Optional[datetime] = None,
                   is_completed: Optional[bool] = None,
                   completion_metadata: Optional[Dict] = None):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        if scheduled_date:
            db_schedule.scheduled_date = scheduled_date
        if is_completed is not None:
            db_schedule.is_completed = is_completed
        if completion_metadata is not None:
            db_schedule.completion_metadata = completion_metadata
        db.commit()
        db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db: Session, schedule_id: int):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        db.delete(db_schedule)
        db.commit()
        return True
    return False

def get_upcoming_schedules(db: Session, student_id: int, limit: int = 10):
    current_time = datetime.now()
    return db.query(Schedule)\
        .filter(Schedule.student_id == student_id)\
        .filter(Schedule.scheduled_date > current_time)\
        .filter(Schedule.is_completed == False)\
        .order_by(Schedule.scheduled_date)\
        .limit(limit).all()

def get_overdue_schedules(db: Session, student_id: int):
    current_time = datetime.now()
    return db.query(Schedule)\
        .filter(Schedule.student_id == student_id)\
        .filter(Schedule.scheduled_date < current_time)\
        .filter(Schedule.is_completed == False)\
        .order_by(Schedule.scheduled_date)\
        .all()

def mark_schedule_completed(db: Session, schedule_id: int, 
                          completion_metadata: Optional[Dict] = None):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        db_schedule.is_completed = True
        if completion_metadata:
            db_schedule.completion_metadata = completion_metadata
        db.commit()
        db.refresh(db_schedule)
    return db_schedule

def reschedule_lesson(db: Session, schedule_id: int, new_date: datetime):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        db_schedule.scheduled_date = new_date
        db_schedule.is_completed = False  # Reset completion status when rescheduling
        db.commit()
        db.refresh(db_schedule)
    return db_schedule