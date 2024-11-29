from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from routes.activityLog import crud, schemas
from database import get_db

router = APIRouter(
    prefix="/activity-logs",
    tags=["activity-logs"]
)

@router.post("/", response_model=schemas.ActivityLog)
def create_activity_log(
    activity_log: schemas.ActivityLogCreate,
    db: Session = Depends(get_db)
):
    return crud.create_activity_log(
        db=db,
        user_id=activity_log.user_id,
        activity_type=activity_log.activity_type,
        description=activity_log.description,
        points_earned=activity_log.points_earned,
        activity_log_metadata=activity_log.activity_log_metadata
    )

@router.get("/{log_id}", response_model=schemas.ActivityLog)
def read_activity_log(log_id: int, db: Session = Depends(get_db)):
    db_log = crud.get_activity_log(db, log_id=log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Activity log not found")
    return db_log

@router.get("/user/{user_id}", response_model=List[schemas.ActivityLog])
def read_user_activity_logs(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    logs = crud.get_user_activity_logs(db, user_id=user_id, skip=skip, limit=limit)
    return logs

@router.patch("/{log_id}", response_model=schemas.ActivityLog)
def update_activity_log(
    log_id: int,
    activity_log: schemas.ActivityLogUpdate,
    db: Session = Depends(get_db)
):
    db_log = crud.update_activity_log(
        db=db,
        log_id=log_id,
        description=activity_log.description,
        points_earned=activity_log.points_earned,
        activity_log_metadata=activity_log.activity_log_metadata
    )
    if db_log is None:
        raise HTTPException(status_code=404, detail="Activity log not found")
    return db_log

@router.delete("/{log_id}")
def delete_activity_log(log_id: int, db: Session = Depends(get_db)):
    success = crud.delete_activity_log(db=db, log_id=log_id)
    if not success:
        raise HTTPException(status_code=404, detail="Activity log not found")
    return {"message": "Activity log deleted successfully"}