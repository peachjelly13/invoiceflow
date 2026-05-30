import uuid 
from datetime import datetime
from sqlalchemy import String,Enum as SQAEnum,DateTime
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base,TimestampMixin,PrimaryKeyMixin
import enum

#These are the only user roles allowed in our system

class UserRole(enum.Enum):
    ADMIN = "admin"
    FINANCE_MANAGER = "finance_manager"
    VENDOR = "vendor"

class User(Base, TimestampMixin,PrimaryKeyMixin):
    __tablename__ = "users"
    email:Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )
    hashed_password:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    full_name:Mapped[str]=mapped_column(
        String(255),
        nullable=False
    )
    role:Mapped[UserRole]=mapped_column(
        SQAEnum(UserRole),
        nullable=False
    )
    

     


   
