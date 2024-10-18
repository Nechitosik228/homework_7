from pydantic import BaseModel,Field,model_validator
from datetime import datetime
from fastapi import HTTPException


class CreateEvent(BaseModel):
    title:str
    date:datetime = Field(default=datetime.now())

    @model_validator(mode="after")
    def check_date(self):
        if self.date < datetime.now():
            raise HTTPException(status_code=400, detail="Example bad request.")
        return self


class EditEvent(CreateEvent):
    ...


class RescheduleEvent(BaseModel):
    date:datetime = Field(default=datetime.now())

    @model_validator(mode="after")
    def check_date(self):
        if self.date < datetime.now():
            raise HTTPException(status_code=400, detail="Example bad request.")
        return self
    

class RegisterForEvent(BaseModel):
    name:str
    
        