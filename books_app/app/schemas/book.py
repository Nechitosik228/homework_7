from pydantic import BaseModel,Field



class CreateBook(BaseModel):
    name:str = Field(max_length=100)
    author:str = Field(min_length=5,max_length=50)
    release_year:int = Field(le=2024)
    books_quantity:int = Field(gt=0)
