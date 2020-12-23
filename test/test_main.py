from fastapi.testclient import TestClient
from main import app
import random
from database import mycursor, mydb

# variables


randint = random.randint(111111111, 999999999)
num = "09" + str(randint)
name = "xxx"
int1 = 100
int2 = 2

client = TestClient(app)

# end 1


def test_e1_1():
    response = client.post("/add/?name="+name+"&phone="+num)
    assert response.status_code == 200
    assert response.json() == {
        "User added": {
            "Username": name,
            "PhoneNumber": num}
            }
    mycursor.execute("DELETE FROM users WHERE phone = %s", (num,))
    mydb.commit()


def test_e1_2():
    response = client.post("/add/?name=''&phone=09784516627")
    assert response.status_code == 422


def test_e1_3():
    sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
    val = (name, num)
    mycursor.execute(sql, val)
    mydb.commit()
    response = client.post("/add/?name="+name+"&phone="+num)
    assert response.status_code == 406
    assert response.json() == {"detail": "Phone Number is registered"}
    mycursor.execute("DELETE FROM users WHERE phone = %s", (num,))
    mydb.commit()

# end 2


def test_e2_1():
    sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
    val = (name, num)
    mycursor.execute(sql, val)
    mydb.commit()
    response = client.get("/read/")
    assert response.status_code == 200
    assert response.json() == {"Users": [[name, num]]}
    mycursor.execute("DELETE FROM users WHERE phone = %s", (num,))
    mydb.commit()

# end 3


def test_e3_1():
    sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
    val = (name, num)
    mycursor.execute(sql, val)
    mydb.commit()
    response = client.delete("/del/?phone="+num)
    assert response.status_code == 200
    assert response.json() == {"User is deleted": [name, num]}
    mycursor.execute("DELETE FROM users WHERE phone = %s", (num,))
    mydb.commit()


def test_e3_2():
    response = client.delete("/del/?phone="+num)
    assert response.status_code == 406

# end 4


def test_e4_1():
    response = client.put("/change_username/?name="+name+"&phone="+num)
    assert response.status_code == 406


def test_e4_2():
    sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
    val = (name, num)
    mycursor.execute(sql, val)
    mydb.commit()
    response = client.put("/change_username/?name=asghar&phone="+num)
    assert response.status_code == 200
    assert response.json() == {
        "User": [name, num],
        "Username updated to ": "asghar"
        }
    mycursor.execute("DELETE FROM users WHERE phone = %s", (num,))
    mydb.commit()

# end 5


def test_e5_1():
    response = client.get("/div/?a=100&b=2")
    assert response.status_code == 200
    assert response.json() == {"Divition": 50}
