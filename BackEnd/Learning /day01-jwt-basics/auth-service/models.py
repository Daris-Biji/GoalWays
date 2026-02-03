from datetime import datetime, timezone
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User (Base):
    __tablename__ = "users"
    id:Mapped[int] =  mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50),unique=True,index=True)
    hashed_password: Mapped[str] = mapped_column(String (5000))
    created_at:Mapped[datetime] = mapped_column()


