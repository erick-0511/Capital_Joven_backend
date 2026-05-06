from fastapi import APIRouter, Depends, HTTPException, status
from app.services.goal_service import GoalService
from app.core.database import get_database
from app.api.dependencies.deps import get_current_user_from_cookie
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(prefix="/goal", tags=["Goal"])

async def get_goal_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return GoalService(db)