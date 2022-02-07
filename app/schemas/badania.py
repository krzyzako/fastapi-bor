from datetime import datetime
from typing import Any, Dict, List, Optional

import pydantic

# from app.untils import BadanieUntil


class Rodzaj(pydantic.BaseModel):
    # id: int
    nazwa: str


class Homolog(pydantic.BaseModel):
    # id: int
    symbol: str = pydantic.Field(example="W2B")
    nr_homolog: str
    wysokosc: int
    szerokosc: int
    pojemnosc: int
    waga: float
    procent: float
    rodzaj: Optional[Rodzaj]


class Pomiar(pydantic.BaseModel):
    id: Any
    woda: Any
    cisnienie: Any


class Zbiornik(pydantic.BaseModel):
    # id: int
    # symbol: Optional[str]
    numer: str
    homolog: Homolog
    pomiary: List[Pomiar]
    max_woda: Optional[float]
    max_cisnienie: Optional[int]
    procent: Optional[float]
    is_pass: Optional[bool]

    # @pydantic.root_validator
    # def calculate_total_score(
    #     cls,
    #     values,
    # ):
    #     return BadanieUntil.check(values)

    # @pydantic.root_validator
    # def valid_symbol(
    #     cls,
    #     values,
    # ):
    #     print("fgfd", cls, values)
    #     values["symbol"] = values["homolog"].symbol
    #     return values

    # @pydantic.validator("is_pass", always=True)
    # def check_is_pass(cls, v, values):
    #     print("sas", cls.max_woda)


class BadanieSchema(pydantic.BaseModel):
    # id: int
    nr_odbioru: int
    nr_rozrywania: int
    data: datetime
    zbiornik: Zbiornik


class BadanieEXE(pydantic.BaseModel):

    nr_odbioru: int
    nr_rozrywania: int
    data: datetime
    numer: str
    symbol: str
    badania: int
    is_complite = bool

    def __init__(self, **data: BadanieSchema) -> None:
        data["numer"] = data["zbiornik"]["numer"]
        data["symbol"] = data["zbiornik"]["homolog"]["symbol"]
        data["badania"] = len(data["zbiornik"]["pomiary"])
        super().__init__(**data)

    @pydantic.root_validator
    def calculate_total_score(cls, values):
        if values.get("badania") < 5:
            values["is_complite"] = False
        else:
            values["is_complite"] = True
        return values


class BadaniaList(pydantic.BaseModel):
    __root__: List[BadanieSchema]

    # def __init__(self, **data):
    #     print(data["__root__"])
    #     super().__init__(**data)

    def chek(self):
        return self.dict()
