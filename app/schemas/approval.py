import pydantic
from app.models.approval import Rodzaje


Re_Rodzaj = Rodzaje.get_pydantic(exclude={'homologacje'})

class Homolog(pydantic.BaseModel):
    class Config:
        orm_mode = True

    symbol : str
    nr_homolog : str
    wysokosc : int 
    szerokosc : int 
    pojemnosc : int 
    waga : float 
    rodzaj : int