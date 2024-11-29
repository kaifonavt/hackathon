from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from . import crud, schemas

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"]
)

@router.get("/", response_model=List[schemas.Schedule])
def get_all_schedules(db: Session = Depends(get_db)):
    return crud.get_all_schedules(db)
