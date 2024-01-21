from pydantic import BaseModel
from typing import List


class ImageClass(BaseModel):
    class_id: int
    class_name: str


class ClassificationRequest(BaseModel):
    image: str
    location: dict
    device: dict


class ClassificationResponse(BaseModel):
    classes: List[ImageClass]
