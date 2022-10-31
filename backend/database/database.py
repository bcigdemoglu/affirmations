# from typing import List, Union

# from beanie import PydanticObjectId

import os

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.affirmation import Affirmation

affirmation_collection = Affirmation

# TODO: Implement this
# async def init() -> None:
#     # Create Motor client
#     client = AsyncIOMotorClient(
#         os.getenv("MONGODB_URI") or "mongodb://user:pass@host:27017"
#     )

#     # Initialize beanie with Affirmations collection and db
#     print("initializing beanie")
#     await init_beanie(database=client.affirmations, document_models=[Affirmation])
#     print("initialized beanie")

# async def add_affirmation(new_affirmation: Affirmation) -> Affirmation:
#     affirmation = await new_affirmation.create()
#     return affirmation

# async def get_random_affirmation() -> Affirmation:
#     affirmation = await affirmation_collection.find_all().limit(1).to_list()
#     return affirmation[0]


# async def add_student(new_student: Student) -> Student:
#     student = await new_student.create()
#     return student


# async def retrieve_student(id: PydanticObjectId) -> Student:
#     student = await student_collection.get(id)
#     if student:
#         return student


# async def delete_student(id: PydanticObjectId) -> bool:
#     student = await student_collection.get(id)
#     if student:
#         await student.delete()
#         return True


# async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
#     des_body = {k: v for k, v in data.items() if v is not None}
#     update_query = {"$set": {
#         field: value for field, value in des_body.items()
#     }}
#     student = await student_collection.get(id)
#     if student:
#         await student.update(update_query)
#         return student
#     return False
