import mysql.connector
from config import config

mydb = mysql.connector.connect(
    host = config.DB_settings.DB_HOST,
    user = config.DB_settings.DB_USER,
    password = config.DB_settings.USER_PASSWORD,
    database = config.DB_settings.DB_NAME
)

mycursor = mydb.cursor()

