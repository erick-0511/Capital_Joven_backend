from fastapi import APIRouter, Depends, HTTPException, status
from app.core.database import get_database
from app.api.dependencies.deps import get_current_user_from_cookie
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.services.goal_service import GoalService
from app.schemas.goal_schema import CreateGoal, AddAmountGoal, UpdateGoal, ResponseGoal

router = APIRouter(prefix="/goal", tags=["Goal"])

async def get_goal_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return GoalService(db)

@router.post("/register", response_model=ResponseGoal, status_code=status.HTTP_201_CREATED)
async def register_goal(goal_data: CreateGoal, 
                        service: GoalService = Depends(get_goal_service), 
                        current_user: dict = Depends(get_current_user_from_cookie)):
    
    try:
        return await service.register_goal(goal_data.model_dump(), current_user["id_user"])
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al registrar la meta: {str(e)}"            
        )


@router.put("/update/{goal_id}", response_model=ResponseGoal)
async def update_goal(goal_id: str, 
                      goal_update: UpdateGoal, 
                      service: GoalService = Depends(get_goal_service),
                      current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        return await service.update_goal(goal_update.model_dump(exclude_unset=True), 
                                         goal_id,
                                         current_user["id_user"])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar la meta: {str(e)}")
    
@router.delete("/delete/{goal_id}", response_model=dict)
async def delete_goal(goal_id: str, 
                      goal_delete: ResponseGoal, 
                      service: GoalService = Depends(get_goal_service),
                      current_user: dict = Depends(get_current_user_from_cookie)):
    try:    
        return await service.delete_goal(goal_delete.model_dump(exclude_unset=True), 
                                         goal_id,
                                         current_user["id_user"])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la meta: {str(e)}")
    
@router.put("/add/{goal_id}", response_model=ResponseGoal)
async def add_amount(goal_id: str, 
                     data:AddAmountGoal, 
                     service: GoalService = Depends(get_goal_service), 
                     current_user: dict = Depends(get_current_user_from_cookie)):
    
    try:
        return await service.add_amount(
            goal_id,
            data.amount,
            current_user["id_user"]            
        )

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al actualizar la meta: {str(e)}"
        )