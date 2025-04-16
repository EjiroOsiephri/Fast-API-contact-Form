from pydantic import BaseModel
from typing import List, Dict


class ContactCreate(BaseModel):
    name: str
    email: str
    message: str
    phone: str
    whatsapp: str
    preferred_contact: str

class Detail(BaseModel):
    year: str
    scope: str
    interior_feature: List[str]
    exterior_feature: List[str]

class PropertyCreate(BaseModel):
    title: str
    location: str
    paragraph: str
    specification: List[str]
    detail: Detail

class PropertyOut(PropertyCreate):
    images: List[str]

    class Config:
        from_attributes = True