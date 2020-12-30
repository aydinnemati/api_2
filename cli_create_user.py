import typer
from database import mydb, mycursor
import re
ImportError

def create_user(
name: str = typer.Argument(
    ...,
    help="Name of user you want to add"
    ),
phone: int = typer.Argument(
    None,
    help="The phone number of the user  [required]"
        )
    ):
        if phone:
            if phone >= 9000000000 and phone <= 9999999999:
                num = "0"+str(phone)
                mycursor.execute("SELECT * FROM users where phone = %s", (num,))
                check_user = mycursor.fetchone()
                if check_user is None :
                    sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
                    val = (name, num)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    ending = typer.style(
                        "User --(("+name+" "+str(phone)+"))-- Added",
                        fg=typer.colors.GREEN ,
                        bold=True
                        )
                    typer.echo(ending)
                else:
                    raise ValueError(typer.style("Phone number existed", fg=typer.colors.RED, bold=True))
            else:
                raise ValueError(typer.style("Invalid phone number", fg=typer.colors.RED, bold=True))
        else:
            num = typer.prompt(
                "Enter your phone number [09xxxxxxxxx]?"
                )
            if int(num):
                if re.search("^09.........", num):
                    mycursor.execute("SELECT * FROM users where phone = %s", (num,))
                    check_user = mycursor.fetchone()
                    if check_user is None :
                        sql = 'INSERT INTO users (Username, phone) VALUES (%s, %s)'
                        val = (name, num)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        ending = typer.style(
                            "User --(("+name+" "+str(num)+"))-- Added",
                            fg=typer.colors.GREEN ,
                            bold=True
                            )
                        typer.echo(ending)
                    else:
                        raise ValueError(typer.style("Phone number existed", fg=typer.colors.RED, bold=True))
                else:
                    raise ValueError(typer.style("Invalid phone number", fg=typer.colors.RED, bold=True))
if __name__ == "__main__":
    typer.run(create_user)



# ending = typer.style("User Added", fg=typer.colors.MAGENTA  , blink=True