# app.py
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.routing import Mount
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.responses import FileResponse, JSONResponse

from .database import database
from .ilayda.generator import query_openai
from .models.affirmation import Affirmation, DealtIssue

app: FastAPI = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="static")


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

# Define route returning JSON response


@app.get("/")
async def home() -> JSONResponse:
    # Return JSONResponse
    return JSONResponse(content={"message": "Kalbim ILOMMMM"})


@app.get("/get-index")
async def get_index() -> FileResponse:
    return FileResponse('frontend/index.html')


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
