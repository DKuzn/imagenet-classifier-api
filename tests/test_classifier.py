import os
import sys

import pytest

from api.classifier import ImageClassifier
from api.image_processing import ImageProcessing

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_load_valid_model():
    model_path: str = "./api/models/mobilenetv3s.onnx"
    model = ImageClassifier(model_path)


def test_load_invalid_model():
    model_path: str = "./api/models/mobilenv3s.onnx"

    with pytest.raises(Exception) as e_info:
        model = ImageClassifier(model_path)


def test_prediction():
    classifier = ImageClassifier("./api/models/mobilenetv3s.onnx")
    base64_image: str = open("./tests/test_files/test_base64.txt", 'r').read()
    image = ImageProcessing.decode_base64(base64_image)
    image = ImageProcessing.to_tensor(image)
    output = classifier.predict(image)
    # Получение индекса класса с максимальным значением выхода
    class_index = output[0][0].argmax(0)
    assert class_index == 549
