from passlib.context import CryptContext
from pymongo import MongoClient

from api.db.datamodels import Prediction, PredictionCollection, User, UserUpdate


class DbWrapper:
    def __init__(self) -> None:
        self.client = MongoClient(
            "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
        self.db = self.client.get_database("imagenet_classifier")
        self.users_collection = self.db.get_collection("users")
        self.predictions_collection = self.db.get_collection("predictions")
        self.crypt_context = CryptContext(["bcrypt"])

    def create_user(self, user: User) -> None:
        user.password = self.crypt_context.hash(user.password)
        self.users_collection.insert_one(user.model_dump(by_alias=True, exclude=["id"]))

    def get_user_by_id(self, user_id: str) -> User:
        return User(**self.users_collection.find_one(filter={"_id": user_id}))

    def get_user_by_login(self, user_login: str) -> User:
        return User(**self.users_collection.find_one(filter={"login": user_login}))

    def update_user(self, user_update: UserUpdate):
        pass

    def create_prediction(self, pred: Prediction):
        self.predictions_collection.insert_one(pred.model_dump(by_alias=True, exclude=["id"]))

    def get_predictions_by_user(self, user_login):
        return PredictionCollection(predictions=self.predictions_collection.find(filter={"login": user_login}))
