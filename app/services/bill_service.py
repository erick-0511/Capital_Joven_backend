from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from bson import ObjectId

class BillService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db