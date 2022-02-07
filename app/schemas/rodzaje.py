from typing import List
from pydantic import BaseModel,Field

class RodzajNazwa(BaseModel):
    nazwa : str = Field(example='Walcowy')

class RodzajSchema(RodzajNazwa):
    numer : int = Field(example=4)
    

class RodzajIDSchema(RodzajSchema):
    id : int


class Rodzaje(BaseModel):
    users: List[RodzajSchema]
    