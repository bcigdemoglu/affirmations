# app.py
from fastapi import FastAPI

from .models.affirmation import Affirmation, DealtIssue

app: FastAPI = FastAPI()

async def gen_affirmation(dealt_issue: DealtIssue) -> Affirmation:
    affirmation = "You are awesome"
    return affirmation

@app.get("/")
async def hello() -> dict[str, str]:
    return {"message":"Kalbim ILOMMMM"}

@app.post("/brokensoul")
async def post_dealt_issue(dealt_issue: DealtIssue) -> dict[str, str]:
    affirmation: Affirmation = await gen_affirmation(dealt_issue)
    return {"message":"Kalbim ILOMMMM"}
