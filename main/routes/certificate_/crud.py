from sqlalchemy.orm import Session
from typing import Optional, Dict
from models import Certificate

def create_certificate(db: Session, user_id: int, course_id: int, 
                      certificate_number: str, template_data: Optional[Dict] = None):
    db_certificate = Certificate(
        user_id=user_id,
        course_id=course_id,
        certificate_number=certificate_number,
        template_data=template_data or {}
    )
    db.add(db_certificate)
    db.commit()
    db.refresh(db_certificate)
    return db_certificate

def get_certificate(db: Session, certificate_id: int):
    return db.query(Certificate).filter(Certificate.id == certificate_id).first()

def get_user_certificates(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Certificate).filter(Certificate.user_id == user_id)\
        .offset(skip).limit(limit).all()

def update_certificate(db: Session, certificate_id: int, status: Optional[str] = None, 
                      template_data: Optional[Dict] = None):
    db_certificate = db.query(Certificate).filter(Certificate.id == certificate_id).first()
    if db_certificate:
        if status:
            db_certificate.status = status
        if template_data is not None:
            db_certificate.template_data = template_data
        db.commit()
        db.refresh(db_certificate)
    return db_certificate

def delete_certificate(db: Session, certificate_id: int):
    db_certificate = db.query(Certificate).filter(Certificate.id == certificate_id).first()
    if db_certificate:
        db.delete(db_certificate)
        db.commit()
        return True
    return False