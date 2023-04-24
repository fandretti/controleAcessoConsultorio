from fastapi import APIRouter
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.schemas.salas import SalaRequest, SalaResponse
from db.session import get_db
from db.repository.sala import SalaRepository
from src.models.sala import Sala

router = APIRouter()

@router.get("/", response_model=list[SalaResponse], summary="Lista salas", description="Lista das salas cadastradas")
def find_all(nome: str = None, db: Session = Depends(get_db)):
    if nome is not None:
        salas = SalaRepository.find_by_nome(db, nome)
    else:
        salas = SalaRepository.find_all(db)
    return [SalaResponse.from_orm(sala) for sala in salas]


@router.post("/", response_model=SalaResponse, status_code=status.HTTP_201_CREATED)
def create(request: SalaRequest, db: Session = Depends(get_db)):
    sala = SalaRepository.save(db, Sala(**request.dict()))
    return SalaResponse.from_orm(sala)

@router.get("/{id}", response_model=SalaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    sala = SalaRepository.find_by_id(db, id)
    if not sala:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sala não encontrada"
        )
    
    return SalaResponse.from_orm(sala)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not SalaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sala não encontrada"
        )
    SalaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=SalaResponse)
def update(id: int, request: SalaRequest, db: Session = Depends(get_db)):
    if not SalaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sala não encontrada"
        )
    sala = SalaRepository.save(db, Sala(id=id, **request.dict()))
    return SalaResponse.from_orm(sala)
