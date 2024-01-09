# main.py
from app.models.trip import Trip
from sqlalchemy.orm import Session
from . import crud, models, database
from fastapi import FastAPI, Depends, HTTPException
from app.db.config import database
from app.db.base_class import Base
from app.db import get_db
from app.routes import portal_user,portal_user_type,user,company,company_staff,company_type,vehicle,route,stop,staffrole,service,trip,route_stop_mapping
from app.models import portal_user, user, portal_user_type, company, company_staff,company_type,vehicle,route,stop,staffrole,service,trip,route_stop_mapping

# Initialize database tables
Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include your routes here
app.include_router(portal_user.router, prefix="/portal_users", tags=["portal_users"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(portal_user_type.router, prefix="/portal_user_types", tags=["portal_user_types"])
app.include_router(company.router, prefix="/companies", tags=["companies"])
app.include_router(company_staff.router, prefix="/company_staff", tags=["company_staff"])
app.include_router(vehicle.router, prefix="/vehicles", tags=["vehicles"])
app.include_router(route.router, prefix="/routes", tags=["routes"])
app.include_router(stop.router, prefix="/stops", tags=["stops"])
app.include_router(service.router, prefix="/services", tags=["services"])
app.include_router(trip.router, prefix="/trips", tags=["trips"])
app.include_router(route_stop_mapping.router, prefix="/route_stop_mappings", tags=["route_stop_mappings"])

# Additional routes and configurations can be added here
@app.get("/")
async def read_root():
    return {"message": "Hello, welcome to the Fleet Management API!"}

# Example route for getting all trips
@app.get("/all_trips/", response_model=list[trip.Trip])
async def get_all_trips(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    trips = db.query(Trip).offset(skip).limit(limit).all()
    return trips

#@app.get("/all_trips/", response_model=list[Trip])
#async def get_all_trips(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#    trips = crud.get_all_trips(db, skip=skip, limit=limit)
#    return trips



# Example route for creating a company staff
@app.post("/create_company_staff/", response_model=company_staff.CompanyStaff)
async def create_company_staff(company_staff: company_staff.CompanyStaff, db: Session = Depends(get_db)):
    db_company_staff = company_staff.CompanyStaff(**company_staff.dict())
    db.add(db_company_staff)
    db.commit()
    db.refresh(db_company_staff)
    return db_company_staff

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)