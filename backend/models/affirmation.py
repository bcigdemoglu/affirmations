from typing import Optional

from beanie import Document
from pydantic import BaseModel


class Contributor(BaseModel):
    fullname: Optional[str]
    nickname: Optional[str]
    age: Optional[int]
    city: Optional[str]
    country: Optional[str]

class DealtIssue(BaseModel):
    body: str
    contributor: Optional[Contributor]

class Affirmation(Document):
    dealt_issue: DealtIssue
    affirmation: str

    class Settings:
        name: str = "affirmations"