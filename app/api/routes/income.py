from fastapi import APIRouter, Depends, HTTPException, status
from app.services.income_service import IncomeService
from app.schemas.income_schema import CreateIncome
from app.core.database import get_database
from app.api.dependencies.deps import get_current_user_from_cookie
from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime

router = APIRouter(prefix="/income", tags=["Income"])

async def get_income_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return IncomeService(db)

@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
async def register_income(income_data: CreateIncome, service: IncomeService = Depends(get_income_service), 
                        current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        return await service.register_income(income_data.model_dump(), current_user["id_user"])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Ocurrió un error al registrar la información: {str(e)}")