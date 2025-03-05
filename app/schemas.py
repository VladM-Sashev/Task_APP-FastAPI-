from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostTask(BaseModel):
    title: str
    description: str
    priority: str
    

class UpdateTask(BaseModel):
    title: str
    description: str
    completed: bool
    priority: str

# users functionalities

class PostUser(BaseModel):
    email: EmailStr
    password: str

class UserInfo(BaseModel):
    email : EmailStr
    id: int
    created_at: datetime

class TaskResponse(PostTask):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserInfo
    
    class Config:
        from_attributes = True
    

class TokenData(BaseModel):
    id : Optional[int] = None


    