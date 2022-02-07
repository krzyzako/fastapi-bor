from re import A
from fastapi import Depends, HTTPException, status, APIRouter
from app.service import auth
from app.models.approval import Rodzaje

test_router = APIRouter(
    prefix="/api/test",
    tags=["Testy"],
    # dependencies=[Depends(auth.get_current_user)]
    )

@test_router.get("/")
async def read_rodzaj():
    return await Rodzaje.objects.all()

@test_router.post("/add")
async def add_rodzaj(zbiornik : rodzaje_pydanticIn):
    rodzaj = await Rodzaje.create(**zbiornik.dict(exclude_unset=True))
    return await rodzaje_pydantic.from_tortoise_orm(rodzaj)

@test_router.put('/update')
async def update_rodzaj(rodzaj_id:int, rodzaj : rodzaje_pydanticIn):
    await Rodzaje.filter(id=rodzaj_id).update(**rodzaj.dict(exclude_unset=True))
    return await rodzaje_pydantic.from_queryset_single(Rodzaje.get(id=rodzaj_id))

@test_router.delete('/delete')
async def delete(id_del : int):
    del_rodzaj = await Rodzaje.filter(id=id_del).delete()
    if not del_rodzaj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Brak rodzaju o id {id_del}')
    return {'msg' : f'Usunięto {id_del}'}