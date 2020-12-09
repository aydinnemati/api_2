FROM python:3.8

WORKDIR /app

RUN pip3 install fastapi uvicorn mypy pytest pytest-cov pep8 flake8 mysql-connector-python pydantic curl

COPY . /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


