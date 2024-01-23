# app/routes/portal_user_type.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.portal_user_type import PortalUserType

router = APIRouter()

@router.post("/portal_user_types/")
async def create_portal_user_type(name: str, description: str, additional_info: str = None, db: Session = Depends(get_db)):
    new_portal_user_type = PortalUserType(name=name, description=description, additional_info=additional_info)
    db.add(new_portal_user_type)
    db.commit()
    db.refresh(new_portal_user_type)
    return new_portal_user_type

@router.get("/portal_user_types/{portal_user_type_id}")
async def read_portal_user_type(portal_user_type_id: int, db: Session = Depends(get_db)):
    db_portal_user_type = db.query(PortalUserType).filter(PortalUserType.id == portal_user_type_id).first()
    if db_portal_user_type is None:
        raise HTTPException(status_code=404, detail="PortalUserType not found")
    return db_portal_user_type

@router.get("/portal_user_types/")
async def read_all_portal_user_types(db: Session = Depends(get_db)):
    portal_user_types = db.query(PortalUserType).all()
    return portal_user_types
