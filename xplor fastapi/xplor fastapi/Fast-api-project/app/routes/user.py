# app/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User

router = APIRouter()

@router.post("/users/")
async def create_user(username: str, email: str, password: str, company_id: int, user_type: str, created_at: str, additional_info: str = None, db: Session = Depends(get_db)):
    new_user = User(
        username=username,
        email=email,
        password=password,
        company_id=company_id,
        user_type=user_type,
        created_at=created_at,
        additional_info=additional_info
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/")
async def read_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
