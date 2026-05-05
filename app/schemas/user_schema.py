from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    rol: str = Field(default="user", pattern="^(admin|user|artist)$")
    
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=8)
    
class UserInDB(UserBase):
    id_user: str = Field(alias="_id")
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserLoginResponse(BaseModel):
    token: str
    token_type: str = "session"
    
class UserRegisterResponse(BaseModel):
    name: str
    email: EmailStr
    message: str    
    
class UserProfileResponse(BaseModel):
    id_user : str = Field(alias="_id")
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
        populate_by_name = True