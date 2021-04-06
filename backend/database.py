import os
from typing import Dict

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()  # access .env file
MONGO_URI = os.getenv("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.users
collection = database.get_collection("created_users")


def user_helper(user) -> Dict:
    """Helps to structure the user data."""
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email_address": user["email_address"]
    }


async def insert_user(user_info: Dict) -> Dict:
    """Insert user into the DB."""
    user = await collection.insert_one(user_info)
    new_user = await collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)
