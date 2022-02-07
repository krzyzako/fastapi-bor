from re import A
from typing import List
from unicodedata import name
from fastapi import Depends, HTTPException, status, APIRouter

# from app.service import auth
from app.models.approval import Rodzaje, Rodzaje_Py, Homolog
from app.schemas.approval import Re_Rodzaj
from app.schemas.rodzaje import RodzajIDSchema, RodzajSchema

# from app.service.rodzaje import RodzajService

route_rodzaje = APIRouter(
    prefix="/api/rodzaj",
    tags=["Rodzaje zbiorników"],
    # dependencies=[Depends(auth.get_current_user)]
)


@route_rodzaje.get("/", response_model=List[RodzajIDSchema])
async def read_rodzaj():
    return await RodzajService.get_rodzaj_all()


@route_rodzaje.get("/{id}", response_model=RodzajIDSchema)
async def get_by_id(id: int):
    print(id)
    return await Rodzaje.objects.filter(id=id).first()


@route_rodzaje.post("/add", response_model=RodzajIDSchema)
async def add_rodzaj(zbiornik: RodzajSchema):
    rodzaj = await Rodzaje(**zbiornik.dict()).save()
    return rodzaj


@route_rodzaje.put("/update/{id}")
async def update_rodzaj(id: int, rodzaj: RodzajSchema):
    typ = await Rodzaje.objects.get(id=id)
    return await typ.upsert(**rodzaj.dict())


@route_rodzaje.delete("/delete/{id}")
async def delete(id: int):
    del_rodzaj = await Rodzaje.objects.get_or_none(id=id)
    if not del_rodzaj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brak rodzaju o id {id}",
        )
    await del_rodzaj.delete()
    return {"msg": f"Usunięto {id}"}
