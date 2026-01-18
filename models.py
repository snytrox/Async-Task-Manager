from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.sql import func #func, SQL fonksiyonlarını Python’dan çağırmanın yoludur.
from database import Base

class Task(Base):
    __tablename__="tasks"
    id: Mapped[int]= mapped_column(primary_key=True,index=True)
    title:Mapped[str]= mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(default=None)
    priority:Mapped[str]=mapped_column(default="Medium")# Low, Medium, High
    status:Mapped[str]= mapped_column(default="ToDo")# Low, Medium, High
    is_active:Mapped[bool]= mapped_column(default=True)
    created_at:Mapped[DateTime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
        )
    
