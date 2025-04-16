from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from typing import List
import cloudinary.uploader
from . import schemas, models
from .dependencies import get_db  
import json

router = APIRouter()

@router.post("/properties")
async def create_property(
    title: str = Form(...),
    location: str = Form(...),
    paragraph: str = Form(...),
    specification: str = Form(...),  
    detail: str = Form(...),       
    images: List[UploadFile] = File(...),
    db: Session = Depends(get_db) 
):
    uploaded_urls = []
    for img in images:
        result = cloudinary.uploader.upload(img.file)
        uploaded_urls.append(result["secure_url"])

    property = models.Property(
        title=title,
        location=location,
        paragraph=paragraph,
        specification=json.loads(specification),
        images=uploaded_urls,
        detail=json.loads(detail)
    )
    db.add(property)
    db.commit()
    db.refresh(property)
    return {"success": True, "data": property}

@router.get("/properties", response_model=List[schemas.PropertyOut])
def get_properties(db: Session = Depends(get_db)): 
    return db.query(models.Property).all()
