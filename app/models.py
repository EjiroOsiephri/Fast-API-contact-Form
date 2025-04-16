from sqlalchemy import Column, Integer, String, Text, JSON
from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)
    phone = Column(String)
    whatsapp = Column(String)
    preferred_contact = Column(String)

class Property(Base):
    __tablename__ = 'properties'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    location = Column(String)
    paragraph = Column(Text)
    specification = Column(JSON)  # list of strings
    images = Column(JSON)         # list of Cloudinary URLs
    detail = Column(JSON)     
