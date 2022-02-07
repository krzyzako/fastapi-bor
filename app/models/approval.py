from audioop import reverse
import datetime
from email.policy import default
from lib2to3.pgen2.token import OP
from xmlrpc.client import boolean
import ormar
from typing import Any, Dict, List, Optional, Union

import pydantic
from sqlalchemy import null
from app.db import BaseMeta


class Rodzaje(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    nazwa: Optional[str] = ormar.String(max_length=40)
    numer: Optional[int] = ormar.SmallInteger(unique=True)

    # homolog: fields.ReverseRelation["Homolog"]

    class Meta(BaseMeta):
        tablename = "rodzaje"


class Homolog(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    symbol: str = ormar.String(max_length=8, unique=True)
    nr_homolog: str = ormar.String(max_length=16)
    wysokosc: int = ormar.SmallInteger()
    szerokosc: int = ormar.SmallInteger()
    pojemnosc: int = ormar.SmallInteger(null=False)
    waga: float = ormar.Float()

    rodzaj: Optional[Rodzaje] = ormar.ForeignKey(Rodzaje, related_name="homologacje")
    procent: Optional[float]

    class Meta(BaseMeta):
        tablename = "homolog"

    @pydantic.validator("procent", always=True)
    @classmethod
    def check_consistency(cls, v, values):
        if values["rodzaj"].id < 4:
            v = (values["pojemnosc"] * 8) / 100
        else:
            v = (values["pojemnosc"] * 20) / 100
        return v


class Zbiornik(ormar.Model):
    class Meta(BaseMeta):
        tablename = "zbiorniki"

    id: int = ormar.Integer(primary_key=True)
    numer: str = ormar.String(max_length=4, min_length=4)
    homolog: Homolog = ormar.ForeignKey(Homolog, related_name="zbiorniki")


class NumerBadania(ormar.Model):
    class Meta(BaseMeta):
        tablename = "nr_badania"

    id: int = ormar.Integer(primary_key=True)
    nr_odbioru: int = ormar.Integer()
    nr_rozrywania: int = ormar.Integer()
    data: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    zbiornik: Optional[Zbiornik] = ormar.ForeignKey(Zbiornik, related_name="badania", uselist=False)


class Badanie(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    woda: float = ormar.Float()
    cisnienie: int = ormar.Integer()
    zbiornik: Zbiornik = ormar.ForeignKey(Zbiornik, related_name="pomiary")

    class Meta(BaseMeta):
        tablename = "badania"


@ormar.pre_save(Badanie)
async def before_save(sender, instance: Badanie, **kwargs):
    print(f"{sender.get_name()}: {instance.json()}: {kwargs}")


Rodzaje_Py = Rodzaje.get_pydantic(
    exclude={
        "id",
    }
)
Homolog_py = Homolog.get_pydantic(exclude={"id", "rodzaj__numer", "rodzaj__nazwa"})
NumerBadaniaInPy = NumerBadania.get_pydantic(exclude={"id", "data"})
