from typing import Optional

from beanie import Document

from .contributor import Contributor


class Affirmation(Document):
    input: str
    output: str
    contributor: Optional[Contributor]

    class Settings:
        name: str = "affirmations"