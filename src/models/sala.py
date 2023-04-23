from typing import List
from datetime import datetime, date, time
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from db.session import Base
#from src.models.reserva import Reserva

class Sala(Base):
    __tablename__ = "salas"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    reservas: Mapped[List["src.models.reserva.Reserva"]] = relationship(back_populates='sala')
    
    def __repr__(self):
        return f'<Sala(id={self.id}, nome={self.nome})>'

    @property
    def reservas_sala(self):
        return [reserva for reserva in self.reservas]
    
    @hybrid_method
    def sala_ocupada(self, data: datetime):
        _diadasemana = data.weekday()
        _data = data.date()
        _hora = data.time()
        
        return any(r.inicio_reserva <= _data <= r.fim_reserva and _diadasemana == r.dia and r.hora_inicio <= _hora <= r.hora_fim for r in self.reservas_sala)
    
    @hybrid_method
    def sala_ocupada_periodo(self, _diadasemana: int, _data_inicio: date, _data_fim: date, _hora_inicio: time, _hora_fim: time):
        for r in self.reservas_sala:
            if _data_inicio <= r.fim_reserva and _data_fim >= r.inicio_reserva:
                if _hora_inicio <= r.hora_fim and _hora_fim >= r.hora_inicio:
                    if _diadasemana == r.dia:
                        return True
        return False