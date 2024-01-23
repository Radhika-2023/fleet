# app/routes/portal_user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.portal_user import PortalUser
from app.db import get_db

router = APIRouter()

@router.post("/portal_users/", response_model=PortalUser)
async def create_portal_user(portal_user: PortalUser, db: Session = Depends(get_db)):
    db_portal_user = PortalUser(**portal_user.dict())
    db.add(db_portal_user)
    db.commit()
    db.refresh(db_portal_user)
    return db_portal_user

@router.get("/portal_users/{portal_user_id}", response_model=PortalUser)
async def get_portal_user(portal_user_id: int, db: Session = Depends(get_db)):
    db_portal_user = db.query(PortalUser).filter(PortalUser.id == portal_user_id).first()
    if db_portal_user is None:
        raise HTTPException(status_code=404, detail="PortalUser not found")
    return db_portal_user
