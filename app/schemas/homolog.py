from typing import List

from pydantic import BaseModel, Field, root_validator, validator
from app.schemas.rodzaje import RodzajIDSchema, RodzajNazwa, RodzajSchema


class HomologInSchema(BaseModel):
    id: int
    symbol: str = Field(example="W2B")
    nr_homolog: str
    wysokosc: int
    szerokosc: int
    pojemnosc: int
    waga: float
    rodzaj: int


class HomologOutSchema(HomologInSchema):
    rodzaj: RodzajIDSchema

    # nazwa : str = Field(...,alias='rodzaj')
    # numer : int = Field(...,alias='rodzaj')

    # @validator('nazwa', always=True, pre=True)
    # def validate_from_id(cls, v):
    #     v = v.dict(by_alias=False)
    #     if not isinstance(v, dict):
    #         raise TypeError('"from" type must be dict')
    #     if 'nazwa' not in v:
    #         raise ValueError('Not found "id" in "from"')
    #     return v['nazwa']

    # @validator('numer',)
    # def validate_from_numer(cls, v):
    #     v = v.dict(by_alias=True)
    #     if not isinstance(v, dict):
    #         raise TypeError('"from" type must be dict')
    #     if 'numer' not in v:
    #         raise ValueError('Not found "id" in "from"')
    #     print(v['numer'])
    #     return int(v['numer'])
