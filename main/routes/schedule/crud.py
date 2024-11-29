# crud/schedule.py
from sqlalchemy.orm import Session
from typing import List
from datetime import time
from models import Schedule

def create_schedule(db: Session, code: str, day_of_week: int, 
                   start_time: time, end_time: time) -> Schedule:
    db_schedule = Schedule(
        code=code,
        day_of_week=day_of_week,
        start_time=start_time,
        end_time=end_time
    )
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def get_all_schedules(db: Session) -> List[Schedule]:
    return db.query(Schedule)\
        .order_by(Schedule.day_of_week, Schedule.start_time)\
        .all()

def delete_all_schedules(db: Session) -> None:
    db.query(Schedule).delete()
    db.commit()