import typer
import os
from database import mydb, mycursor
ImportError
from decouple import config
import datetime

# make "db_backup" directory

date = datetime.datetime.now()
def db_backup(
    db_name: str = typer.Argument(
    ...,
    help="Name of db you want to backup "+
    " # NOTE: if you want to make cron for this script ,"+
    " you sould comment typer confirm lines"
    )
):
        mycursor.execute(
            "SHOW DATABASES LIKE %s",
            (db_name,)
            )
        db_check = mycursor.fetchone()
        # print(db_check)
        if db_check:
            backup = typer.confirm(
                "Are you sure you want to backup "+db_name+" ?",
                abort=True
                )
            # print(backup)
            db_cont = config("DB_HOST")
            if backup == True:
                backup_file = './db_backup/'+db_name+date.strftime("%x").replace("/", "_")
                # print(backup_file)
                typer.echo("backup file : "+ backup_file)
                cmd = 'docker exec -it '+db_cont+' "mysqldump -u {0} -p {1} > {2}"'.format(config("DB_USER"),\
                config("DB_NAME"),backup_file,)
                make_file = "touch "+backup_file 
                os.system(make_file)
                os.system(cmd)
                ending = typer.style(
                            "Getting backup from "+db_name,
                            fg=typer.colors.BRIGHT_YELLOW ,
                            bold=True
                            )
                typer.echo(ending)
        else:
            raise ValueError(
        typer.style(
            "Database "+db_name+" is not existed! check you database name",
            fg=typer.colors.RED, bold=True
                )
            )
if __name__ == "__main__":
    typer.run(db_backup)