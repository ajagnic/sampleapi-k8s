FROM python:latest

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

WORKDIR /app

COPY ./python/ .

CMD ["python", "app.py"]
