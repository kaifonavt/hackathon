from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from routes.certificate_ import crud, schemas

router = APIRouter(
    prefix="/certificates",
    tags=["certificates"]
)

@router.post("/", response_model=schemas.Certificate)
def create_certificate(
    certificate: schemas.CertificateCreate,
    db: Session = Depends(get_db)
):
    return crud.create_certificate(
        db=db,
        user_id=certificate.user_id,
        course_id=certificate.course_id,
        certificate_number=certificate.certificate_number,
        template_data=certificate.template_data
    )

@router.get("/{certificate_id}", response_model=schemas.Certificate)
def read_certificate(certificate_id: int, db: Session = Depends(get_db)):
    db_certificate = crud.get_certificate(db, certificate_id=certificate_id)
    if db_certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return db_certificate

@router.get("/user/{user_id}", response_model=List[schemas.Certificate])
def read_user_certificates(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    certificates = crud.get_user_certificates(db, user_id=user_id, skip=skip, limit=limit)
    return certificates

@router.patch("/{certificate_id}", response_model=schemas.Certificate)
def update_certificate(
    certificate_id: int,
    certificate: schemas.CertificateUpdate,
    db: Session = Depends(get_db)
):
    db_certificate = crud.update_certificate(
        db=db,
        certificate_id=certificate_id,
        status=certificate.status,
        template_data=certificate.template_data
    )
    if db_certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return db_certificate

@router.delete("/{certificate_id}")
def delete_certificate(certificate_id: int, db: Session = Depends(get_db)):
    success = crud.delete_certificate(db, certificate_id=certificate_id)
    if not success:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return {"message": "Certificate deleted successfully"}