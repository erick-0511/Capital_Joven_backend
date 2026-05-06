from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class CategoryBill(str, Enum):
    VIVIENDA = "Vivienda"
    ALIMENTACION = "Alimentación"
    TRANSPORTE = "Transporte"
    SALUD = "Salud"
    ENTRETENIMIENTO = "Entretenimiento"
    ESCUELA = "Escuela"
    RETIROS = "Retiros"
    OTROS = "Otros"
    
class PaymentMethod(str, Enum):
    EFECTIVO = "Efectivo"
    DEBITO = "Débito"
    CREDITO = "Crédito"
    TRANSFERENCIA = "Transferencia"
    
class Frequency(str, Enum):
    UNICO = "Único"
    DIARIO = "Diario"
    SEMANAL = "Semanal"
    QUINCENAL = "Quincenal"
    MENSUAL = "Mensual"
    ANUAL = "Anual"
    
class CreateBill(BaseModel):
    title: str
    amount: float
    date: Optional[datetime] = None
    category: CategoryBill
    method: PaymentMethod
    description: Optional[str] = None
    frequency: Frequency
    
class UpdateBill(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    categoty: Optional[CategoryBill] = None
    mehtod: Optional[PaymentMethod] = None
    description: Optional[str] = None
    frequency: Optional[Frequency] = None
    
class AllBillResponse(BaseModel):
    bill_id: str = Field(alias="_id")
    title: str
    amount: float
    
class BillResponse(BaseModel):
    bill_id: str = Field(alias="_id")
    title: str
    amount: float
    date: datetime
    category: CategoryBill
    method: PaymentMethod
    description: Optional[str] = None
    frequency: Frequency
    
    class Config:
        from_attributes = True
        populate_by_name = True