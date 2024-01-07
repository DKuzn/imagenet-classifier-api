from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: PyObjectId | None = Field(alias="_id", default=None)
    login: str = Field(max_length=100)
    password: str = Field(max_length=200)
    token: str | None = Field(max_length=200)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class PredictionData(BaseModel):
    class_name: str
    probability: float
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class Prediction(BaseModel):
    id: PyObjectId | None = Field(alias="_id", default=None)
    predictions: [PredictionData]
    datetime: str = Field()
    user_id: str = Field()
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
