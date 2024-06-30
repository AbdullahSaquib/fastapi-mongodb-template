from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient


MONGO_CONNECTION_STRING = f"mongodb+srv://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)

db = client[settings.MONGO_DATABASE]
