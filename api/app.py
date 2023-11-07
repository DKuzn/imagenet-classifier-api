from typing import Union

from fastapi import FastAPI
from api.datamodels import ClassificationRequest, ClassificationResponse, ImageClass
from api.image_processing import ImageProcessing

app = FastAPI(title="ImageNet Classifier API")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/classify", response_model=ClassificationResponse)
async def classify(request: ClassificationRequest):
    base64_image: str = request.image
    image = ImageProcessing.decode_base64(base64_image)
    print(f"Image shape {image.shape}")
    return ClassificationResponse(
        classes=[
            ImageClass(class_id=1, class_name="test1"), 
            ImageClass(class_id=2, class_name="test2")
        ]
    )
