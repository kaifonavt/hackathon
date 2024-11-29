from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, Dict

from database import get_db
from routes.portfolio import crud, schemas

router = APIRouter(
    prefix="/portfolios",
    tags=["portfolios"]
)

@router.post("/", response_model=schemas.Portfolio)
def create_portfolio(
    user_id: int,
    portfolio: schemas.PortfolioCreate,
    db: Session = Depends(get_db)
):
    existing_portfolio = crud.get_user_portfolio(db, user_id)
    if existing_portfolio:
        raise HTTPException(status_code=400, detail="User already has a portfolio")
    return crud.create_portfolio(
        db=db,
        user_id=user_id,
        summary=portfolio.summary,
        skills=portfolio.skills,
        achievements_summary=portfolio.achievements_summary
    )

@router.get("/{portfolio_id}", response_model=schemas.Portfolio)
def read_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    db_portfolio = crud.get_portfolio(db, portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db_portfolio

@router.get("/user/{user_id}", response_model=schemas.Portfolio)
def read_user_portfolio(user_id: int, db: Session = Depends(get_db)):
    db_portfolio = crud.get_user_portfolio(db, user_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db_portfolio

@router.patch("/{portfolio_id}", response_model=schemas.Portfolio)
def update_portfolio(
    portfolio_id: int,
    portfolio: schemas.PortfolioUpdate,
    db: Session = Depends(get_db)
):
    db_portfolio = crud.update_portfolio(
        db=db,
        portfolio_id=portfolio_id,
        summary=portfolio.summary,
        skills=portfolio.skills
    )
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db_portfolio

@router.delete("/{portfolio_id}")
def delete_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    success = crud.delete_portfolio(db, portfolio_id)
    if not success:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return {"message": "Portfolio successfully deleted"}