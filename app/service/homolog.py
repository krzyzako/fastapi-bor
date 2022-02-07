from typing import List
from fastapi import HTTPException, status
from ormar import MultipleMatches
import pydantic
from sqlalchemy import null
from app.models.approval import Homolog, Zbiornik
from app.schemas.homolog import (
    HomologInSchema,
    HomologOutSchema,
)


class HomologService:
    @classmethod
    async def read_all(self):
        _orm = await Homolog.objects.select_related("rodzaj").all()
        return pydantic.parse_obj_as(List[HomologOutSchema], _orm)

    @classmethod
    async def read_with_rodzaj(cls):
        return await Homolog.objects.select_related(["rodzaj"]).all()

    @classmethod
    async def find_by_symbol(cls, symbol: str):
        try:
            cls.read_all
            _orm = (
                await Homolog.objects.select_all(
                    [
                        "rodzaj",
                        "zbiorniki",
                        "zbiorniki__badania",
                    ]
                )
                .filter(Homolog.symbol.startswith(symbol.upper()))
                .get_or_none()
            )
        except (MultipleMatches):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"{symbol}  wiele wyników wyszukiwania",
            )

        return _orm
