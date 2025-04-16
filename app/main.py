from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, email_utils, sms_utils
from .routes import router
from .dependencies import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.post("/contact")
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    # Send Email and SMS
    email_utils.send_email(contact)
    sms_utils.send_sms(contact)

    return {"message": "Contact data received and forwarded!"}


