from sqlalchemy.orm import Session
from typing import Optional, Dict
from models import Badge

def create_badge(db: Session, name: str, number: int, description: Optional[str] = None, 
                styles: Optional[Dict] = None, requirements: Optional[Dict] = None):
    db_badge = Badge(
        name=name,
        number=number,
        description=description,
        styles=styles or {},
        requirements=requirements or {}
    )
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge

def get_badge(db: Session, badge_id: int):
    return db.query(Badge).filter(Badge.id == badge_id).first()

def get_badges(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Badge).offset(skip).limit(limit).all()

def update_badge(db: Session, badge_id: int, name: Optional[str] = None, 
                description: Optional[str] = None, styles: Optional[Dict] = None):
    db_badge = db.query(Badge).filter(Badge.id == badge_id).first()
    if db_badge:
        if name:
            db_badge.name = name
        if description is not None:
            db_badge.description = description
        if styles is not None:
            db_badge.styles = styles
        db.commit()
        db.refresh(db_badge)
    return db_badge

def delete_badge(db: Session, badge_id: int):
    db_badge = db.query(Badge).filter(Badge.id == badge_id).first()
    if db_badge:
        db.delete(db_badge)
        db.commit()
        return True
    return False