from sqlalchemy.orm import Session

import models,schemas

def get_plataformas(db: Session):
    return db.query(models.Plataforma).all()

def create_reporte(db: Session, reporte: schemas.ReporteCreate):
    db_reporte = models.Reporte(videojuego=reporte.videojuego, plataforma_id=reporte.plataforma_id)
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte

def get_reportes(db: Session):
    return db.query(models.Reporte).all()