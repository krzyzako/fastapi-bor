from operator import imod
from typing import List
import zipimport

import pydantic
from app.models.approval import NumerBadania
from fastapi import Depends, HTTPException, status, APIRouter
from app.schemas.badania import BadaniaList, BadanieSchema

# from app.service.badania import BadaniaService

router_badania = APIRouter(
    prefix="/api/badania",
    tags=["Próby zbiorników"],
    # dependencies=[Depends(auth.get_current_user)]
)


@router_badania.get("/")
async def read_homolog():
    test = await NumerBadania.objects.select_all(follow=True).all()
    lis = []
    for badania in test:
        lis.append(badania.dict())
    print(lis)
    # test1 = BadaniaList(__root__=lis)
    # test1 =BadaniaService.read_all()
    test = await pydantic.parse_obj_as(List[BadanieSchema], test)
    return test
