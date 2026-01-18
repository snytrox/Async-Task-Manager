#SQLAlchemy veritabanı tarafını temsil eder(models.py),
#Pydantic ise API ile dış dünya arasındaki veri güvenliğini sağlar(schemas.py).
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title:str
    description: Optional[str]= None
    priority: str="Medium"
    status:str="ToDo"
    model_config = ConfigDict(from_attributes=True)
class TaskCreate(TaskBase):
    pass
class TaskResponse(TaskBase):
    id:int
    is_active:bool
    created_at:datetime
