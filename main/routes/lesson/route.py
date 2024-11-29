from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from routes.lesson import crud, schemas

router = APIRouter(
    prefix="/lessons",
    tags=["lessons"]
)

@router.post("/", response_model=schemas.Lesson)
def create_lesson(
    lesson: schemas.LessonCreate,
    db: Session = Depends(get_db)
):
    return crud.create_lesson(
        db=db,
        course_id=lesson.course_id,
        title=lesson.title,
        content=lesson.content,
        order=lesson.order,
        points=lesson.points,
        lesson_metadata=lesson.lesson_metadata
    )

@router.get("/{lesson_id}", response_model=schemas.Lesson)
def read_lesson(lesson_id: int, db: Session = Depends(get_db)):
    db_lesson = crud.get_lesson(db, lesson_id=lesson_id)
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson

@router.get("/", response_model=List[schemas.Lesson])
def read_lessons(
    course_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    lessons = crud.get_lessons(db, course_id=course_id, skip=skip, limit=limit)
    return lessons

@router.patch("/{lesson_id}", response_model=schemas.Lesson)
def update_lesson(
    lesson_id: int,
    lesson: schemas.LessonUpdate,
    db: Session = Depends(get_db)
):
    db_lesson = crud.update_lesson(
        db=db,
        lesson_id=lesson_id,
        title=lesson.title,
        content=lesson.content,
        order=lesson.order
    )
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson

@router.delete("/{lesson_id}")
def delete_lesson(lesson_id: int, db: Session = Depends(get_db)):
    success = crud.delete_lesson(db, lesson_id=lesson_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return {"message": "Lesson deleted successfully"}