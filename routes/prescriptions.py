from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Prescription

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])


@router.get("/")
def list_prescriptions(db: Session = Depends(get_db)):
    return db.query(Prescription).all()


@router.post("/")
def create_prescription(data: dict, db: Session = Depends(get_db)):
    prescription = Prescription(
        visit_id=data.get("visit_id"),
        medication=data.get("medication"),
        dose=data.get("dose"),
        frequency=data.get("frequency"),
        duration=data.get("duration"),
    )
    db.add(prescription)
    db.commit()
    db.refresh(prescription)
    return prescription

