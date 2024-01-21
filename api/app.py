import datetime
import json
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasicCredentials

from api.auth.auth_service import AuthService
from api.classifier import ImageClassifier
from api.datamodels import ClassificationRequest, ClassificationResponse, ImageClass
from api.db.database import DbWrapper
from api.db.datamodels import Prediction, PredictionData
from api.db.router import router as DbRouter
from api.image_processing import ImageProcessing

app = FastAPI(title="ImageNet Classifier API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth_service = AuthService()
db = DbWrapper()

app.include_router(DbRouter)

classifier = ImageClassifier("./api/models/mobilenetv3s.onnx")

with open("./api/models/imagenet_class_index.json") as file:
    classes = json.load(file)


@app.post("/classify", response_model=ClassificationResponse)
async def classify(request: ClassificationRequest, credentials: Annotated[HTTPBasicCredentials, Depends(auth_service.authenticate)]):
    base64_image: str = request.image.split(',')[1]
    image = ImageProcessing.decode_base64(base64_image)
    image = ImageProcessing.to_tensor(image)
    output = classifier.predict(image)
    class_index = output[0][0].argmax(0)
    class_name = classes[str(class_index)][1]

    db_pred = Prediction(
        image=base64_image,
        predictions=[PredictionData(
            class_index=class_index, class_name=class_name)],
        location=request.location,
        device=request.device,
        datetime=str(datetime.datetime.now()),
        login=credentials.username
    )

    db.create_prediction(db_pred)

    return ClassificationResponse(
        classes=[
            ImageClass(class_id=class_index,
                       class_name=class_name),
        ]
    )
