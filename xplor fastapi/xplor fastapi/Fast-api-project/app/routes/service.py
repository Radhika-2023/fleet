# app/routes/service.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.service import Service

router = APIRouter()

@router.post("/services/")
async def create_service(service_name: str, reservation: bool, db: Session = Depends(get_db)):
    new_service = Service(service_name=service_name, reservation=reservation)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.get("/services/{service_id}")
async def read_service(service_id: int, db: Session = Depends(get_db)):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.get("/services/")
async def read_all_services(db: Session = Depends(get_db)):
    services = db.query(Service).all()
    return services
