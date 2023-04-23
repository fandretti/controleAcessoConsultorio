from fastapi import APIRouter
from src.endpoints import salas, solicitante, reservas, salaocupada, reservasala

router = APIRouter()
router.include_router(salas.router, prefix="/api/salas", tags=["salas"])
router.include_router(solicitante.router, prefix="/api/solicitantes", tags=["solicitantes"])
router.include_router(reservas.router, prefix="/api/reservas", tags=["reservas"])
router.include_router(salaocupada.router, prefix="/api/salaocupada", tags=["salaocupada"])
router.include_router(reservasala.router, prefix="/api/reservassala", tags=["reservassala"])