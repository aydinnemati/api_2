# My Api

its a CRUD api on mysql database written by python3.

# Installation and Packages

Use the package manager [pip to install fastapi](https://pypi.org/project/fastapi/).

```bash
pip install fastapi
```
Use the package manager [pip to install uvicorn](https://www.uvicorn.org/).

```bash
pip install uvicorn
```
Use the package manager [pip install pytest-cov](https://pypi.org/project/pytest-cov/).

```bash
pip install pytest-cov
```

and for using models you should [install mysql](https://dev.mysql.com/downloads/installer/).
after installing mysql,you need to change connections settings in code its not recommanded but you can make a database named my_api and a user for it named admin with password admin too. 

# Run App

for runnig this api you can type this command in root directory.
```bash
uvicorn main:app
```
# CI

### for running test 

```bash
pytest --cov main
```
### coverage :
```bash
pytest --cov main
```
### linter

##### pep8

```bash
pep8 main.py
```
##### flake8

```bash
flake8 main.py
```
##### mypy

```bash
mypy main.py
```

# Contributing

post and get requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

