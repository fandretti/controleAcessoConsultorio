from sqlalchemy.orm import Session
from typing import List
from src.models.sala import Sala

class SalaRepository:
    @staticmethod
    def find_all(db: Session) -> List[Sala]:
        return db.query(Sala).all()

    @staticmethod
    def save(db: Session, sala: Sala) -> Sala:
        if sala.id:
            db.merge(sala)
        else:
            db.add(sala)
        db.commit()
        return sala

    @staticmethod
    def find_by_id(db: Session, id: int) -> Sala:
        return db.query(Sala).filter(Sala.id == id).first()
    
    @staticmethod
    def find_by_nome(db: Session, nome: str) -> Sala:
        return db.query(Sala).filter(Sala.nome == nome).all()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Sala).filter(Sala.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        sala = db.query(Sala).filter(Sala.id == id).first()
        if sala is not None:
            db.delete(sala)
            db.commit()