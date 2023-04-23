from pydantic import BaseModel

class SalaBase(BaseModel):
    nome: str

class SalaRequest(SalaBase):
    ...

class SalaResponse(SalaBase):
    id: int

    class Config:
        orm_mode = True