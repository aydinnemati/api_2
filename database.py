import mysql.connector # type: ignore
from decouple import config # type: ignore

mydb = mysql.connector.connect(
    # host = config("DB_HOST"),
    host = config("DB_HOST"),
    # port = config("DB_PORT"), 
    user = config("DB_USER"),
    password = config("USER_PASSWORD"),
    database = config("DB_NAME")
)

mycursor = mydb.cursor()

# check if table exists

table = []
mycursor.execute("SHOW TABLES LIKE 'users'")
for x in mycursor:
    table.append(x)
if table == []:
    mycursor.execute(
        "CREATE TABLE users (Username VARCHAR(255) NOT NULL,"
        + "phone VARCHAR(255) NOT NULL UNIQUE)"
        )
