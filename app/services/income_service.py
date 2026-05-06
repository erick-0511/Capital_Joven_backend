from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime, timezone
from bson import ObjectId

class IncomeService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        
    async def register_income(self, income_data: dict, user_id: str):
        income_data.update({"date": datetime.now(timezone.utc), "user_id": user_id})
        income_result = await self.db.income.insert_one(income_data)
        if income_result.inserted_id:
            return {"message": "El ingreso se ha registrado correctamente."}
        raise ValueError("Ocurrio un error al registrar el ingreso.")