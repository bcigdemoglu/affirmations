# app.py
from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
def hello() -> dict[str, str]:
    return {"message":"Kalbim ILOMMMM"}