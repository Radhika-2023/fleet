# app/routes/route.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.route import Route

router = APIRouter()

@router.post("/routes/")
async def create_route(route_description: str, additional_info: str = None, db: Session = Depends(get_db)):
    new_route = Route(route_description=route_description, additional_info=additional_info)
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route

@router.get("/routes/{route_id}")
async def read_route(route_id: int, db: Session = Depends(get_db)):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return db_route

@router.get("/routes/")
async def read_all_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()
    return routes
