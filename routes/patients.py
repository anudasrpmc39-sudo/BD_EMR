from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Patient

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/")
def list_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()


@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.post("/")
def create_patient(data: dict, db: Session = Depends(get_db)):
    patient = Patient(
        patient_id=data.get("patient_id"),
        full_name=data.get("full_name"),
        date_of_birth=data.get("date_of_birth"),
        sex=data.get("sex"),
        phone=data.get("phone"),
        address=data.get("address"),
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

