# My Api

its a CRUD api on mysql database written by python3.


# Run App

docker build -t poj2 .
docker-compose up -d

# CI

### for running test :

```bash
pytest --cov main
```
### coverage :
```bash
python3 -m pytest --cov |grep  "^main.py"
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

put,post and get requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

