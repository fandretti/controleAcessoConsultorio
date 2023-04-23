from typing import List
from datetime import datetime, date, time
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from db.session import Base
#from src.models.reserva import Reserva // Comentado para evitar import circular com o model sala. Usando o caminho completo o sqlalchemy entende mesmo sem o import

class Solicitante(Base):
    __tablename__ = "solicitantes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    tag: Mapped[str] = mapped_column(String(30), unique=True)

    reservas: Mapped[List["src.models.reserva.Reserva"]] = relationship(back_populates='solicitante')

    def __repr__(self):
        return f'<Solicitante(id={self.id}, nome={self.nome}, email={self.email}, tag={self.tag})>'