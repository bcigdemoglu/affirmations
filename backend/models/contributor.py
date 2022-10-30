from typing import Optional

from beanie import Document


class Contributor(Document):
    fullname: Optional[str]
    nickname: Optional[str]
    age: Optional[int]
    city: Optional[str]
    country: Optional[str]
    coords: Optional[tuple[float, float]]

    class Settings:
        name = "contributors"
