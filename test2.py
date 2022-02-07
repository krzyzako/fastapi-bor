import ormar
import csv
import aiofiles
from aiocsv import AsyncDictReader
import sqlalchemy
import asyncio

from app.db import BaseMeta, database, metadata,engine
from app.models.approval import Homolog, Rodzaje

async def main():
    async with database:
        # tw = await Rodzaje(nazwa='Teroidalny wewnętrzny', numer=1).save()
        # tz = await Rodzaje(nazwa='Teroidalny zewnętrzny', numer=2).save()
        # tzp = await Rodzaje(nazwa='Teroidalny zewnętrzny pełny', numer=3).save()
        # w = await Rodzaje(nazwa='Walcowy', numer=4).save()
    
        async with aiofiles.open("homolog.csv", mode="r", encoding="utf-8", newline="") as afp:
            async for row in AsyncDictReader(afp):
                zb = await Homolog(
                    symbol = row['symbol'],
                    nr_homolog = row['approval'],
                    wysokosc = row['height'],
                    waga =row['weight'],
                    szerokosc = row['dimeter'],
                    pojemnosc = row['capacity'],
                    rodzaj = int(row['tank'])
                ).save()

asyncio.run(main())