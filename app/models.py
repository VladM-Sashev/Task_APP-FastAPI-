from pydantic import BaseModel
from sqlalchemy import Column,Integer,String,Boolean, ForeignKey
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)  
    title = Column(String, nullable=False)  
    description = Column(String, nullable=True)  
    completed = Column(Boolean, server_default=text("FALSE"), nullable=False)  
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))  
    priority = Column(String,nullable=False)
    owner_id = Column(Integer, ForeignKey("UsersTasks.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
class User(Base):
    __tablename__ = 'UsersTasks'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))