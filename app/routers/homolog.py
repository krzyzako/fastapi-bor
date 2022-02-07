from typing import List
from fastapi import Depends, HTTPException, status, APIRouter
from app.models.approval import Homolog
from app.schemas.homolog import HomologInSchema
from app.service.homolog import HomologService

router_homolog = APIRouter(
    prefix="/api/homolog",
    tags=["Homologacje"],
    # dependencies=[Depends(auth.get_current_user)]
)


@router_homolog.get("/")
async def read_homolog():
    return await HomologService.read_all()


@router_homolog.get(
    "/find/{symbol}",
)
async def find_by_symbol(symbol: str):
    print(symbol)
    return await HomologService.find_by_symbol(symbol=symbol)


@router_homolog.post("/add", response_model=Homolog)
async def add_homolog(homolog: HomologInSchema):
    homolog = await Homolog(**homolog.dict()).save()
    await homolog.load()
    return homolog


@router_homolog.put("/update/{homolog_id}")
async def update_homolog(homolog_id: int, homolog: HomologInSchema):
    badanie = await Homolog.objects.filter(id=homolog_id).first()
    print(homolog.dict(exclude_unset=True))
    return await badanie.upsert(**homolog.dict())


@router_homolog.delete("/delete/{id_del}")
async def delete(id_del: int):
    del_homolog = await Homolog.objects.get_or_none(id=id_del)
    if not del_homolog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brak rodzaju o id {id_del}",
        )
    await del_homolog.delete()
    return {"msg": f"Usunięto {id_del}"}
