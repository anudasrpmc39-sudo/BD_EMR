from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Visit

router = APIRouter(prefix="/visits", tags=["Visits"])


@router.get("/")
def list_visits(db: Session = Depends(get_db)):
    return db.query(Visit).all()


@router.post("/")
def create_visit(data: dict, db: Session = Depends(get_db)):
    visit = Visit(
        patient_id_fk=data.get("patient_id_fk"),
        visit_date=data.get("visit_date"),
        chief_complaint=data.get("chief_complaint"),
        diagnosis=data.get("diagnosis"),
        notes=data.get("notes"),
    )
    db.add(visit)
    db.commit()
    db.refresh(visit)
    return visit

