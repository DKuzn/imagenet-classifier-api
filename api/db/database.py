from api.db.datamodels import User, Prediction, PredictionData
from motor.motor_asyncio import AsyncIOMotorClient


class DbWrapper:
    client = AsyncIOMotorClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
    db = client.get_database("imagenet_classifier")
    users_collection = db.get_collection("users")
    predictions_collection = db.get_collection("predictions")

    async def get_users(cls):
        return cls.users_collection.find_one()

    def get_users_by_id(cls, user_id):
        pass
