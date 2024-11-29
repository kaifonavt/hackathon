from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from routes.personalGoal import crud, schemas
from database import get_db

router = APIRouter(
    prefix="/goals",
    tags=["goals"]
)

@router.post("/", response_model=schemas.PersonalGoal)
def create_goal(
    goal: schemas.PersonalGoalCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.create_personal_goal(
        db=db,
        user_id=user_id,
        title=goal.title,
        target_date=goal.target_date,
        description=goal.description,
        progress_data=goal.progress_data
    )

@router.get("/{goal_id}", response_model=schemas.PersonalGoal)
def read_goal(goal_id: int, db: Session = Depends(get_db)):
    db_goal = crud.get_personal_goal(db, goal_id=goal_id)
    if db_goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal

@router.get("/user/{user_id}", response_model=List[schemas.PersonalGoal])
def read_user_goals(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    goals = crud.get_user_goals(db, user_id=user_id, skip=skip, limit=limit)
    return goals

@router.patch("/{goal_id}", response_model=schemas.PersonalGoal)
def update_goal(
    goal_id: int,
    goal_update: schemas.PersonalGoalUpdate,
    db: Session = Depends(get_db)
):
    db_goal = crud.update_personal_goal(
        db=db,
        goal_id=goal_id,
        title=goal_update.title,
        description=goal_update.description,
        status=goal_update.status
    )
    if db_goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal

@router.delete("/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    success = crud.delete_personal_goal(db, goal_id=goal_id)
    if not success:
        raise HTTPException(status_code=404, detail="Goal not found")
    return {"message": "Goal successfully deleted"}