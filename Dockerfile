FROM python:latest

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

WORKDIR /app

COPY ./python/ .

EXPOSE 5001

CMD ["python", "app.py"]
