from pydantic import BaseModel

class ContactCreate(BaseModel):
    name: str
    email: str
    message: str
    phone: str
    whatsapp: str
    preferred_contact: str
