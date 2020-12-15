FROM python:3.8

COPY . /app

RUN pip3 install -r /app/requirements.txt 

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


