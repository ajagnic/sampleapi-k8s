FROM python:latest

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

WORKDIR /app

COPY ./python/ .

ENV MONGODB_URI mongodb://localhost:27017

EXPOSE 5001

CMD ["python", "app.py"]
