from typing import List
from datetime import datetime, date, time
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from db.session import Base
from src.models.sala import Sala
from src.models.solicitante import Solicitante

class Reserva(Base):
    __tablename__ = "reservas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sala_id: Mapped["Sala"] = mapped_column(ForeignKey("salas.id"))
    sala: Mapped["Sala"] = relationship(back_populates="reservas")
    inicio_reserva: Mapped["date"] = mapped_column(Date)
    fim_reserva: Mapped["date"] = mapped_column(Date)
    dia: Mapped[int] = mapped_column(Integer)
    hora_inicio: Mapped["time"] = mapped_column(Time)
    hora_fim: Mapped["time"] = mapped_column(Time)    
    solicitante_id: Mapped["Solicitante"] = mapped_column(ForeignKey("solicitantes.id"))
    solicitante: Mapped["Solicitante"] = relationship(back_populates="reservas")
    
    def __repr__(self):
        return f'<Reserva(id={self.id}, sala_id={self.sala_id}, solicitante_id={self.solicitante_id}, inicio_reserva={self.inicio_reserva}, fim_reserva={self.fim_reserva}, dia={self.dia}, hora_inicio={self.hora_inicio}, hora_fim={self.hora_fim})>'