from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API Controle de Acesso Consultorio"
    app_version: str = "0.0.1"
    project_version: str = app_version
    project_name: str = "Controle de Acesso Consultorio"
    admin_email: str = "fandretti@gmail.com"


settings = Settings()