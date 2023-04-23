from pydantic import BaseModel
from datetime import date, time
from src.schemas.salas import SalaResponse
from src.schemas.solicitantes import SolicitanteResponse

class ReservaBase(BaseModel):
    sala_id: int
    solicitante_id: int
    inicio_reserva: date
    fim_reserva: date
    dia: int
    hora_inicio: time
    hora_fim: time
    

class ReservaRequest(ReservaBase):
    ...

class ReservaResponse(BaseModel):
    id: int
    inicio_reserva: date
    fim_reserva: date
    dia: int
    hora_inicio: time
    hora_fim: time
    sala: SalaResponse
    solicitante: SolicitanteResponse

    class Config:
        orm_mode = True