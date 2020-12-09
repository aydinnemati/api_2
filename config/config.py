from pydantic import BaseSettings
 # localhost
# class db_settings(BaseSettings):
#     DB_HOST: str = "127.0.0.1"
#     DB_USER: str = "admin"
#     USER_PASSWORD: str = "admin"
#     DB_NAME: str = "my_api"


# DB_settings = db_settings()



class db_settings(BaseSettings):
    DB_HOST: str = "mysql_comp"
    DB_PORT: str = "3306"
    DB_USER: str = "admin"
    USER_PASSWORD: str = "admin"
    DB_NAME: str = "doc_api_1"


DB_settings = db_settings()