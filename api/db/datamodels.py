from typing import List

from pydantic import BaseModel, ConfigDict, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: PyObjectId | None = Field(alias="_id", default=None)
    login: str = Field(max_length=100)
    password: str = Field(max_length=200)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class UserUpdate(BaseModel):
    login: str | None = Field(max_length=100)
    password: str | None = Field(max_length=200)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class PredictionData(BaseModel):
    class_name: str
    class_index: int
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class Location(BaseModel):
    latitude: float
    longitude: float


class Prediction(BaseModel):
    id: PyObjectId | None = Field(alias="_id", default=None)
    image: str
    predictions: List[PredictionData]
    location: Location
    device: dict
    datetime: str = Field()
    login: str = Field()
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class PredictionCollection(BaseModel):
    predictions: List[Prediction]
