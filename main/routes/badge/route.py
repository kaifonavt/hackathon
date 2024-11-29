from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from routes.badge import crud, schemas

router = APIRouter(
    prefix="/badges",
    tags=["badges"]
)

@router.post("/", response_model=schemas.Badge)
def create_badge(badge: schemas.BadgeCreate, db: Session = Depends(get_db)):
    return crud.create_badge(
        db=db,
        name=badge.name,
        number=badge.number,
        description=badge.description,
        styles=badge.styles,
        requirements=badge.requirements
    )

@router.get("/{badge_id}", response_model=schemas.Badge)
def read_badge(badge_id: int, db: Session = Depends(get_db)):
    db_badge = crud.get_badge(db, badge_id=badge_id)
    if db_badge is None:
        raise HTTPException(status_code=404, detail="Badge not found")
    return db_badge

@router.get("/", response_model=List[schemas.Badge])
def read_badges(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    badges = crud.get_badges(db, skip=skip, limit=limit)
    return badges

@router.patch("/{badge_id}", response_model=schemas.Badge)
def update_badge(
    badge_id: int,
    badge_update: schemas.BadgeUpdate,
    db: Session = Depends(get_db)
):
    db_badge = crud.update_badge(
        db=db,
        badge_id=badge_id,
        name=badge_update.name,
        description=badge_update.description,
        styles=badge_update.styles
    )
    if db_badge is None:
        raise HTTPException(status_code=404, detail="Badge not found")
    return db_badge

@router.delete("/{badge_id}")
def delete_badge(badge_id: int, db: Session = Depends(get_db)):
    success = crud.delete_badge(db, badge_id=badge_id)
    if not success:
        raise HTTPException(status_code=404, detail="Badge not found")
    return {"message": "Badge deleted successfully"}