from typing import Union

from fastapi import FastAPI
from api.datamodels import ClassificationRequest, ClassificationResponse, ImageClass
from api.image_processing import ImageProcessing
from api.classifier import ImageClassifier
import json

app = FastAPI(title="ImageNet Classifier API")

classifier = ImageClassifier("./api/models/mobilenetv3s.onnx")

with open("./api/models/imagenet_class_index.json") as file:
    classes = json.load(file)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/classify", response_model=ClassificationResponse)
async def classify(request: ClassificationRequest):
    base64_image: str = request.image
    image = ImageProcessing.decode_base64(base64_image)
    image = ImageProcessing.to_tensor(image)
    output = classifier.predict(image)
    class_index = output[0][0].argmax(0)
    return ClassificationResponse(
        classes=[
            ImageClass(class_id=class_index, class_name=classes[str(class_index)][1]), 
        ]
    )
