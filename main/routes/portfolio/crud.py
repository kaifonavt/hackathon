from sqlalchemy.orm import Session
from typing import Optional, Dict
from models import Portfolio

def create_portfolio(db: Session, user_id: int, summary: Optional[str] = None, 
                    skills: Optional[Dict] = None, achievements_summary: Optional[Dict] = None):
    db_portfolio = Portfolio(
        user_id=user_id,
        summary=summary,
        skills=skills or {},
        achievements_summary=achievements_summary or {}
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

def get_portfolio(db: Session, portfolio_id: int):
    return db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()

def get_user_portfolio(db: Session, user_id: int):
    return db.query(Portfolio).filter(Portfolio.user_id == user_id).first()

def update_portfolio(db: Session, portfolio_id: int, summary: Optional[str] = None, 
                    skills: Optional[Dict] = None):
    db_portfolio = db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
    if db_portfolio:
        if summary is not None:
            db_portfolio.summary = summary
        if skills is not None:
            db_portfolio.skills = skills
        db.commit()
        db.refresh(db_portfolio)
    return db_portfolio

def delete_portfolio(db: Session, portfolio_id: int):
    db_portfolio = db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
    if db_portfolio:
        db.delete(db_portfolio)
        db.commit()
        return True
    return False