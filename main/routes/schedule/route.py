from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Dict, List, Optional
from datetime import datetime

from database import get_db
import routes.schedule.crud as schedule_crud
from routes.schedule.schemas import Schedule, ScheduleCreate, ScheduleUpdate

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"]
)

@router.post("/", response_model=Schedule)
def create_schedule(
    schedule: ScheduleCreate,
    db: Session = Depends(get_db)
):
    return schedule_crud.create_schedule(
        db=db,
        student_id=schedule.student_id,
        lesson_id=schedule.lesson_id,
        scheduled_date=schedule.scheduled_date,
        completion_metadata=schedule.completion_metadata
    )

@router.get("/{schedule_id}", response_model=Schedule)
def get_schedule(
    schedule_id: int,
    db: Session = Depends(get_db)
):
    db_schedule = schedule_crud.get_schedule(db, schedule_id=schedule_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule

@router.get("/student/{student_id}", response_model=List[Schedule])
def get_student_schedules(
    student_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    db: Session = Depends(get_db)
):
    return schedule_crud.get_student_schedules(
        db, 
        student_id=student_id,
        skip=skip,
        limit=limit
    )

@router.get("/lesson/{lesson_id}", response_model=List[Schedule])
def get_lesson_schedules(
    lesson_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    db: Session = Depends(get_db)
):
    return schedule_crud.get_lesson_schedules(
        db,
        lesson_id=lesson_id,
        skip=skip,
        limit=limit
    )

@router.patch("/{schedule_id}", response_model=Schedule)
def update_schedule(
    schedule_id: int,
    schedule_update: ScheduleUpdate,
    db: Session = Depends(get_db)
):
    db_schedule = schedule_crud.update_schedule(
        db=db,
        schedule_id=schedule_id,
        scheduled_date=schedule_update.scheduled_date,
        is_completed=schedule_update.is_completed,
        completion_metadata=schedule_update.completion_metadata
    )
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule

@router.delete("/{schedule_id}")
def delete_schedule(
    schedule_id: int,
    db: Session = Depends(get_db)
):
    success = schedule_crud.delete_schedule(db, schedule_id=schedule_id)
    if not success:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"message": "Schedule deleted successfully"}

@router.get("/student/{student_id}/upcoming", response_model=List[Schedule])
def get_upcoming_schedules(
    student_id: int,
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    return schedule_crud.get_upcoming_schedules(
        db,
        student_id=student_id,
        limit=limit
    )

@router.get("/student/{student_id}/overdue", response_model=List[Schedule])
def get_overdue_schedules(
    student_id: int,
    db: Session = Depends(get_db)
):
    return schedule_crud.get_overdue_schedules(
        db,
        student_id=student_id
    )

@router.post("/{schedule_id}/complete", response_model=Schedule)
def mark_schedule_completed(
    schedule_id: int,
    completion_metadata: Optional[Dict] = None,
    db: Session = Depends(get_db)
):
    db_schedule = schedule_crud.mark_schedule_completed(
        db,
        schedule_id=schedule_id,
        completion_metadata=completion_metadata
    )
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule

@router.post("/{schedule_id}/reschedule", response_model=Schedule)
def reschedule_lesson(
    schedule_id: int,
    new_date: datetime,
    db: Session = Depends(get_db)
):
    db_schedule = schedule_crud.reschedule_lesson(
        db,
        schedule_id=schedule_id,
        new_date=new_date
    )
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule