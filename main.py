# FastAPI with uvicorn example
#
# start with 
#     uvicorn main:app  --reload --port=8080 --host=0.0.0.0
#     http://localhost:8080/docs to see swagger docs

from fastapi import FastAPI
from os import environ as env

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Host is {env['HOSTNAME']}"}

@app.get("/showenv")
async def root():
    return {"message": f"payload test = {env}"}


 
os.walk():
