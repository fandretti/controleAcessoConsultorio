from sqlalchemy.orm import Session
from src.models.reserva import Reserva
from typing import List

class ReservaRepository:
    @staticmethod
    def find_all(db: Session) -> List[Reserva]:
        return db.query(Reserva).all()

    @staticmethod
    def save(db: Session, reserva: Reserva) -> Reserva:
        if reserva.id:
            db.merge(reserva)
        else:
            db.add(reserva)
        db.commit()
        return reserva

    @staticmethod
    def find_by_id(db: Session, id: int) -> Reserva:
        return db.query(Reserva).filter(Reserva.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Reserva).filter(Reserva.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        reserva = db.query(Reserva).filter(Reserva.id == id).first()
        if reserva is not None:
            db.delete(reserva)
            db.commit()