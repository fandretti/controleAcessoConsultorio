from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from db.session import get_db
from src.schemas.reservas import ReservaRequest, ReservaResponse
from src.models.reserva import Reserva
from db.repository.sala import SalaRepository
from db.repository.reserva import ReservaRepository

router = APIRouter()

@router.post("/", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
def create(request: ReservaRequest, db: Session = Depends(get_db)):
    _reserva_to_create = Reserva(**request.dict())
    sala = SalaRepository.find_by_id(db, _reserva_to_create.sala_id)
    if not sala:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sala não encontrada"
        )
    
    if sala.sala_ocupada_periodo(_reserva_to_create.dia, _reserva_to_create.inicio_reserva, _reserva_to_create.fim_reserva, _reserva_to_create.hora_inicio, _reserva_to_create.hora_fim):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Sala ocupada"
        )
    reserva = ReservaRepository.save(db, _reserva_to_create)
    return ReservaResponse.from_orm(reserva)

@router.get("/", response_model=list[ReservaResponse])
def find_all(db: Session = Depends(get_db)):
    reservas = ReservaRepository.find_all(db)
    return [ReservaResponse.from_orm(reserva) for reserva in reservas]

@router.get("/{id}", response_model=ReservaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    reserva = ReservaRepository.find_by_id(db, id)
    if not reserva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="reserva não encontrada"
        )
    return ReservaResponse.from_orm(reserva)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ReservaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada"
        )
    ReservaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=ReservaResponse)
def update(id: int, request: ReservaRequest, db: Session = Depends(get_db)):
    if not ReservaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada"
        )
    reserva = ReservaRepository.save(db, Reserva(id=id, **request.dict()))
    return ReservaResponse.from_orm(reserva)
