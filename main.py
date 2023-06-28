from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

#delete middleware in production
from fastapi.middleware.cors import CORSMiddleware

origins = ['http://localhost:4200']

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#delete middleware in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/plataforma", response_model=list[schemas.Plataforma])
def read_plataformas(db: Session = Depends(get_database_session)):
    return crud.get_plataformas(db)

@app.post("/reporte", response_model=schemas.ReporteBase)
def write_reporte(reporte: schemas.ReporteCreate, db: Session = Depends(get_database_session)):
    return crud.create_reporte(db, reporte)

@app.get("/reporte", response_model=list[schemas.Reporte])
def read_reportes(db: Session = Depends(get_database_session)):
    return crud.get_reportes(db)