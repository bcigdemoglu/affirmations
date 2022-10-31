# app.py
import os

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .database import database
from .ilayda.generator import query_openai
from .models.affirmation import Affirmation, DealtIssue

app: FastAPI = FastAPI()

async def gen_affirmation(dealt_issue: DealtIssue) -> Affirmation:
    affirm_text: str = await query_openai(dealt_issue.text)
    affirmation: Affirmation = Affirmation(
        dealt_issue=dealt_issue, affirmation=affirm_text
        )
    # TODO: Connect to DB
    # await database.add_affirmation(affirmation)
    return affirmation

@app.on_event("startup")
async def app_init():
    # TODO: INIT BEANIE
    # await database.init()
    pass

@app.get("/")
async def hello() -> dict[str, str]:
    return {"message":"Kalbim ILOMMMM"}

@app.post("/get-affirmation")
async def post_dealt_issue(dealt_issue: DealtIssue) -> Affirmation:
    return await gen_affirmation(dealt_issue)

@app.get("/random-affirmation")
async def get_random_affirmation() -> Affirmation:
    return await gen_affirmation(DealtIssue(text="life"))

# TODO: Implement this
# @app.get("/past-affirmation")
# async def get_past_affirmation() -> Affirmation:
#     return database.get_random_affirmation()

