from sqlalchemy.orm import Session
from typing import Optional, Dict
from datetime import date
from models import PersonalGoal

def create_personal_goal(db: Session, user_id: int, title: str, target_date: date,
                        description: Optional[str] = None, progress_data: Optional[Dict] = None):
    db_goal = PersonalGoal(
        user_id=user_id,
        title=title,
        description=description,
        target_date=target_date,
        progress_data=progress_data or {}
    )
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def get_personal_goal(db: Session, goal_id: int):
    return db.query(PersonalGoal).filter(PersonalGoal.id == goal_id).first()

def get_user_goals(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(PersonalGoal).filter(PersonalGoal.user_id == user_id)\
        .offset(skip).limit(limit).all()

def update_personal_goal(db: Session, goal_id: int, title: Optional[str] = None,
                        description: Optional[str] = None, status: Optional[str] = None):
    db_goal = db.query(PersonalGoal).filter(PersonalGoal.id == goal_id).first()
    if db_goal:
        if title:
            db_goal.title = title
        if description is not None:
            db_goal.description = description
        if status:
            db_goal.status = status
        db.commit()
        db.refresh(db_goal)
    return db_goal

def delete_personal_goal(db: Session, goal_id: int):
    db_goal = db.query(PersonalGoal).filter(PersonalGoal.id == goal_id).first()
    if db_goal:
        db.delete(db_goal)
        db.commit()
        return True
    return False