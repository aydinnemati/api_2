import mysql.connector
from config import config

mydb = mysql.connector.connect(
    host=config.DB_settings.DB_HOST,
    # port=config.DB_settings.DB_PORT, 
    user=config.DB_settings.DB_USER,
    password=config.DB_settings.USER_PASSWORD,
    database = config.DB_settings.DB_NAME
)

mycursor = mydb.cursor()

# check if database exists

table = []
mycursor.execute("SHOW DATABASES LIKE %s",
                (config.DB_settings.DB_NAME, )
                )
for x in mycursor:
    table.append(x)
if table == []:
    mycursor.execute(
        "CREATE DATABASE "+config.DB_settings.DB_NAME 
    )

# check if table exists

mycursor.execute("USE "+config.DB_settings.DB_NAME)
table = []
mycursor.execute("SHOW TABLES LIKE 'users'")
for x in mycursor:
    table.append(x)
if table == []:
    mycursor.execute(
        "CREATE TABLE users (Username VARCHAR(255) NOT NULL,"
        + "phone VARCHAR(255) NOT NULL UNIQUE)"
        )
