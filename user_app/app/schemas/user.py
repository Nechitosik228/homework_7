from pydantic import BaseModel,Field,EmailStr,model_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from string import punctuation


class CreateUser(BaseModel):
    name:str = Field(min_length=2)
    surname:str = Field(min_length=2)
    email:EmailStr
    password:str = Field(min_length=8)
    phone_number:PhoneNumber


    @model_validator(mode="after")
    def check_model(self):
        pswd=self.password
        if not any(c.isupper() for c in pswd):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(c.islower() for c in pswd):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in pswd):
            raise ValueError("Password must have at least one digit")
        if not any(c in punctuation for c in pswd):
            raise ValueError("Password must have at least one special char")
        return self


