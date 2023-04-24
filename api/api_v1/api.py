from fastapi import APIRouter
from api.api_v1.endpoints import salas, solicitantes, reservas, salaocupada, reservasala

router = APIRouter()
router.include_router(salas.router, prefix="/salas", tags=["salas"])
router.include_router(solicitantes.router, prefix="/solicitantes", tags=["solicitantes"])
router.include_router(reservas.router, prefix="/reservas", tags=["reservas"])
router.include_router(salaocupada.router, prefix="/salaocupada", tags=["salaocupada"])
router.include_router(reservasala.router, prefix="/reservassala", tags=["reservassala"])