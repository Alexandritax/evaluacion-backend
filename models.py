from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from database import Base

class Plataforma(Base):
    __tablename__ = 'plataforma'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Reporte(Base):
    __tablename__ = 'reporte'
    id = Column(Integer, primary_key=True, index=True)
    videojuego = Column(String, unique=True, nullable=False)
    plataforma_id = Column(Integer, ForeignKey('plataforma.id'))
    plataforma = Relationship("Plataforma")