FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# CMD uvicorn main:app --reload --port=8080 --host=0.0.0.0
 
CMD uvicorn main:app --reload --port=${PORT} --host=0.0.0.0
