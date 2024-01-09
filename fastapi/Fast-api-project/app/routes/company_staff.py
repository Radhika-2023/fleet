# app/routes/company_staff.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.company_staff import CompanyStaff

router = APIRouter()

@router.post("/company_staff/")
async def create_company_staff(
    first_name: str, middle_name: str, last_name: str, fleet_owner_id: int,
    staff_role_id: int, email_id: str, phone: int, otp_receive_time: str,
    additional_info: str = None, db: Session = Depends(get_db)
):
    new_company_staff = CompanyStaff(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        fleet_owner_id=fleet_owner_id,
        staff_role_id=staff_role_id,
        email_id=email_id,
        phone=phone,
        otp_receive_time=otp_receive_time,
        additional_info=additional_info
    )
    db.add(new_company_staff)
    db.commit()
    db.refresh(new_company_staff)
    return new_company_staff

@router.get("/company_staff/{company_staff_id}")
async def read_company_staff(company_staff_id: int, db: Session = Depends(get_db)):
    db_company_staff = db.query(CompanyStaff).filter(CompanyStaff.id == company_staff_id).first()
    if db_company_staff is None:
        raise HTTPException(status_code=404, detail="CompanyStaff not found")
    return db_company_staff

@router.get("/company_staff/")
async def read_all_company_staff(db: Session = Depends(get_db)):
    company_staff_members = db.query(CompanyStaff).all()
    return company_staff_members
