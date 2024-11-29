from typing import Dict, Optional
from pydantic import BaseModel

class CertificateBase(BaseModel):
    user_id: int
    course_id: int
    certificate_number: str
    template_data: Optional[Dict] = {}

class CertificateCreate(CertificateBase):
    pass

class CertificateUpdate(BaseModel):
    status: Optional[str] = None
    template_data: Optional[Dict] = None

class Certificate(CertificateBase):
    id: int
    status: Optional[str] = None

    class Config:
        from_attributes = True