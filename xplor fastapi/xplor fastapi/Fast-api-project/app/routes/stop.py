
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.stop import Stop

router = APIRouter()

@router.post("/stops/")
async def create_stop(stop_name: str, latitude: float, longitude: float, city: str, district: str, state: str, pincode: int, stop_owner_id: int, additional_info: str = None, db: Session = Depends(get_db)):
    new_stop = Stop(
        stop_name=stop_name,
        latitude=latitude,
        longitude=longitude,
        city=city,
        district=district,
        state=state,
        pincode=pincode,
        stop_owner_id=stop_owner_id,
        additional_info=additional_info
    )
    db.add(new_stop)
    db.commit()
    db.refresh(new_stop)
    return new_stop

@router.get("/stops/{stop_id}")
async def read_stop(stop_id: int, db: Session = Depends(get_db)):
    db_stop = db.query(Stop).filter(Stop.id == stop_id).first()
    if db_stop is None:
        raise HTTPException(status_code=404, detail="Stop not found")
    return db_stop

@router.get("/stops/")
async def read_all_stops(db: Session = Depends(get_db)):
    stops = db.query(Stop).all()
    return stops
