from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from src.schemas.solicitantes import SolicitanteRequest, SolicitanteResponse
from db.session import get_db
from db.repository.solicitante import SolicitanteRepository
from src.models.solicitante import Solicitante

router = APIRouter()

@router.post("/", response_model=SolicitanteResponse, status_code=status.HTTP_201_CREATED)
def create(request: SolicitanteRequest, db: Session = Depends(get_db)):
    solicitante = SolicitanteRepository.save(db, Solicitante(**request.dict()))
    return SolicitanteResponse.from_orm(solicitante)

@router.get("/", response_model=list[SolicitanteResponse])
def find_all(db: Session = Depends(get_db)):
    solicitantes = SolicitanteRepository.find_all(db)
    return [SolicitanteResponse.from_orm(solicitante) for solicitante in solicitantes]

@router.get("/{id}", response_model=SolicitanteResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    solicitante = SolicitanteRepository.find_by_id(db, id)
    if not solicitante:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="solicitante não encontrado"
        )
    return SolicitanteResponse.from_orm(solicitante)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not SolicitanteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="solicitante não encontrado"
        )
    SolicitanteRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=SolicitanteResponse)
def update(id: int, request: SolicitanteRequest, db: Session = Depends(get_db)):
    if not SolicitanteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="solicitante não encontrado"
        )
    solicitante = SolicitanteRepository.save(db, Solicitante(id=id, **request.dict()))
    return SolicitanteResponse.from_orm(solicitante)
