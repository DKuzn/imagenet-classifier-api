import os
import sys

from api.classifier import ImageClassifier
import pytest

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
