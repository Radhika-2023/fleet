# app/routes/trip.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.trip import Trip

router = APIRouter()

@router.post("/trips/")
async def create_trip(trip_name: str, start_time: str, end_time: str, db: Session = Depends(get_db)):
    new_trip = Trip(trip_name=trip_name, start_time=start_time, end_time=end_time)
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip

@router.get("/trips/{trip_id}")
async def read_trip(trip_id: int, db: Session = Depends(get_db)):
    db_trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return db_trip

@router.get("/trips/")
async def read_all_trips(db: Session = Depends(get_db)):
    trips = db.query(Trip).all()
    return trips
