from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import LabResult

router = APIRouter(prefix="/labs", tags=["Laboratory Results"])


@router.get("/")
def list_labs(db: Session = Depends(get_db)):
    return db.query(LabResult).all()


@router.post("/")
def create_lab_result(data: dict, db: Session = Depends(get_db)):
    lab = LabResult(
        visit_id=data.get("visit_id"),
        test_name=data.get("test_name"),
        result=data.get("result"),
        unit=data.get("unit"),
        reference_range=data.get("reference_range"),
    )
    db.add(lab)
    db.commit()
    db.refresh(lab)
    return lab

