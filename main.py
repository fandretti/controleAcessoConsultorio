import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router
from db.session import Base, engine
from core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    print(f"Executando {settings.app_name}: {settings.app_version}")
    print(f"Autor: {settings.admin_email}")
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="debug", reload=True)