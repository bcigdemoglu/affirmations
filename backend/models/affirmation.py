# from typing import Optional

from beanie import Document
from pydantic import BaseModel

# TODO: Implement this
# class Contributor(BaseModel):
#     fullname: Optional[str]
#     nickname: Optional[str]
#     age: Optional[int]
#     city: Optional[str]
#     country: Optional[str]

class DealtIssue(BaseModel):
    text: str
    # TODO: add contributor info
    # contributor: Optional[Contributor]

class Affirmation(BaseModel):
    dealt_issue: DealtIssue
    affirmation: str
