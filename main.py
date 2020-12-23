from fastapi import FastAPI, Query, HTTPException
from database import mycursor, mydb

app = FastAPI()

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

# add user - endpoint 1


@app.post("/add/")
def add_user(name: str = Query(
                            ...,
                            min_length=1,
                            regex="^[a-z/A-Z]"
                              ),
             phone: str = Query(
                            ...,
                            min_length=11,
                            max_length=11,
                            regex="^09")):
    mycursor.execute("SELECT * FROM users where phone = %s", (phone,))
    check_phone = mycursor.fetchone()
    if check_phone:
        raise HTTPException(
            status_code=406,
            detail="Phone Number is registered")
    else:
        sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
        val = (name, phone)
        mycursor.execute(sql, val)
        mydb.commit()
        return {"User added": {"Username": name, "PhoneNumber": phone}}

# list users - endpoint 2


@app.get("/read/")
def show_users():
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    listt = []
    for x in myresult:
        listt.append(x)
    dictt = {"Users": listt}
    return dictt

# delete users - endpoint 3


@app.delete("/del/")
def del_user(phone: str = Query(
                                ...,
                                min_length=11,
                                max_length=11,
                                regex="^09")):
    mycursor.execute("SELECT * FROM users where phone = %s", (phone,))
    check_user = mycursor.fetchone()
    if check_user is None:
        raise HTTPException(status_code=406, detail="User is not existed")
    else:
        mycursor.execute("DELETE FROM users WHERE phone = %s", (phone,))
        mydb.commit()
        return {"User is deleted": check_user}

# delete users - endpoint 4


@app.put("/change_username/")
def update_username(name: str = Query(
                                    ...,
                                    min_length=1,
                                    regex="^[a-z/A-Z]"
                                     ),
                    phone: str = Query(
                                    ...,
                                    min_length=11,
                                    max_length=11,
                                    regex="^09")):
    mycursor.execute("SELECT * FROM users where phone = %s", (phone,))
    check_user = mycursor.fetchone()
    if check_user is None:
        raise HTTPException(
            status_code=406,
            detail="User is not existed"
            )
    else:
        mycursor.execute(
            "UPDATE users SET Username = %s WHERE phone = %s", (name, phone)
            )
        mydb.commit()
        return {"User": check_user, "Username updated to ": name}

# numbers divition - endpoint 5


@app.get("/div/")
def divition(a: float, b: float = Query(..., gt=0)):
    divition = a/b
    return {"Divition": divition}
