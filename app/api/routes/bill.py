from fastapi import APIRouter, Depends, HTTPException, status
from app.services.bill_service import BillService
from app.core.database import get_database
from app.api.dependencies.deps import get_current_user_from_cookie
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(prefix="/bill", tags=["Bill"])

async def get_bill_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return BillService(db)