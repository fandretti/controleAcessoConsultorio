from sqlalchemy.orm import Session
from src.models.solicitante import Solicitante
from typing import List

class SolicitanteRepository:
    @staticmethod
    def find_all(db: Session) -> List[Solicitante]:
        return db.query(Solicitante).all()

    @staticmethod
    def save(db: Session, solicitante: Solicitante) -> Solicitante:
        if solicitante.id:
            db.merge(solicitante)
        else:
            db.add(solicitante)
        db.commit()
        return solicitante

    @staticmethod
    def find_by_id(db: Session, id: int) -> Solicitante:
        return db.query(Solicitante).filter(Solicitante.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Solicitante).filter(Solicitante.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        solicitante = db.query(Solicitante).filter(Solicitante.id == id).first()
        if solicitante is not None:
            db.delete(solicitante)
            db.commit()