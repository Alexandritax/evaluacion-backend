from pydantic import BaseModel

class PlataformaBase(BaseModel):
    name: str

class Plataforma(PlataformaBase):
    id: int

    class Config:
        orm_mode = True

class ReporteCreate(BaseModel):
    videojuego: str
    plataforma_id: int


class ReporteBase(ReporteCreate):
    id: int

    class Config:
        orm_mode = True


class Reporte(ReporteBase):
    name: str

    class Config:
        orm_mode = True