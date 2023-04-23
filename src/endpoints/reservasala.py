from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from typing import List
from src.schemas.reservas import ReservaResponse
from db.session import get_db
from db.repository.sala import SalaRepository
from src.models.sala import Sala

router = APIRouter()

@router.get("/{id}", response_model=List[ReservaResponse])
def find_by_id(id: int, db: Session = Depends(get_db)):
    sala = SalaRepository.find_by_id(db, id)
    if not sala:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sala não encontrada"
        )
    reservas = sala.reservas_sala
    
    return reservas