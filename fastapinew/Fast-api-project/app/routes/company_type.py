# app/routes/company_type.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.company_type import CompanyType

router = APIRouter()

@router.post("/company_types/")
async def create_company_type(
    name: str, description: str, additional_info: str = None, db: Session = Depends(get_db)
):
    new_company_type = CompanyType(name=name, description=description, additional_info=additional_info)
    db.add(new_company_type)
    db.commit()
    db.refresh(new_company_type)
    return new_company_type

@router.get("/company_types/{company_type_id}")
async def read_company_type(company_type_id: int, db: Session = Depends(get_db)):
    db_company_type = db.query(CompanyType).filter(CompanyType.id == company_type_id).first()
    if db_company_type is None:
        raise HTTPException(status_code=404, detail="CompanyType not found")
    return db_company_type

@router.get("/company_types/")
async def read_all_company_types(db: Session = Depends(get_db)):
    company_types = db.query(CompanyType).all()
    return company_types
