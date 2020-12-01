from pydantic import BaseSettings

class db_settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_USER: str = "admin"
    USER_PASSWORD: str = "admin"
    DB_NAME: str = "my_api"


DB_settings = db_settings()