from pydantic import BaseModel

class SolicitanteBase(BaseModel):
    nome: str
    email: str
    tag: str

class SolicitanteRequest(SolicitanteBase):
    ...

class SolicitanteResponse(SolicitanteBase):
    id: int
    
    class Config:
        orm_mode = True