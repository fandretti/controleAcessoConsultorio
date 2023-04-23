from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from typing import List
from datetime import datetime
from db.session import get_db
from db.repository.sala import SalaRepository
#from models import Sala

router = APIRouter()

@router.get("/{id}")
def sala_ocupada(id: int, datahora: datetime = None, db: Session = Depends(get_db)):
    sala = SalaRepository.find_by_id(db, id)
    if not sala:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sala não encontrada"
        )
    if datahora is not None:
        return sala.sala_ocupada(datahora)
    else:
        return sala.sala_ocupada(datetime.now())