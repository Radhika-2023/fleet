# app/routes/vehicle.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.vehicle import Vehicle

router = APIRouter()

@router.post("/vehicles/")
async def create_vehicle(vehicle_number: str, vehicle_description: str, permit_number: str, capacity: int, pos_id: int, gps_id: int, service_id: int, fleet_owner_id: int, additional_info: str = None, db: Session = Depends(get_db)):
    new_vehicle = Vehicle(
        vehicle_number=vehicle_number,
        vehicle_description=vehicle_description,
        permit_number=permit_number,
        capacity=capacity,
        pos_id=pos_id,
        gps_id=gps_id,
        service_id=service_id,
        fleet_owner_id=fleet_owner_id,
        additional_info=additional_info
    )
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

@router.get("/vehicles/{vehicle_id}")
async def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@router.get("/vehicles/")
async def read_all_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).all()
    return vehicles
