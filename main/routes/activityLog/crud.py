from sqlalchemy.orm import Session
from typing import Optional, Dict
from models import ActivityLog

def create_activity_log(db: Session, user_id: int, activity_type: str,
                       description: Optional[str] = None, points_earned: int = 0,
                       activity_log_metadata: Optional[Dict] = None):
    db_log = ActivityLog(
        user_id=user_id,
        activity_type=activity_type,
        description=description,
        points_earned=points_earned,
        activity_log_metadata=activity_log_metadata or {}
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_activity_log(db: Session, log_id: int):
    return db.query(ActivityLog).filter(ActivityLog.id == log_id).first()

def get_user_activity_logs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(ActivityLog).filter(ActivityLog.user_id == user_id)\
        .order_by(ActivityLog.created_at.desc())\
        .offset(skip).limit(limit).all()

def update_activity_log(db: Session, log_id: int, description: Optional[str] = None,
                       points_earned: Optional[int] = None,
                       activity_log_metadata: Optional[Dict] = None):
    db_log = db.query(ActivityLog).filter(ActivityLog.id == log_id).first()
    if db_log:
        if description is not None:
            db_log.description = description
        if points_earned is not None:
            db_log.points_earned = points_earned
        if activity_log_metadata is not None:
            db_log.activity_log_metadata = activity_log_metadata
        db.commit()
        db.refresh(db_log)
    return db_log

def delete_activity_log(db: Session, log_id: int):
    db_log = db.query(ActivityLog).filter(ActivityLog.id == log_id).first()
    if db_log:
        db.delete(db_log)
        db.commit()
        return True
    return False
