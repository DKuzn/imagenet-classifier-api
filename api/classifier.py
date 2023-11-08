import onnx
import onnxruntime as ort
import numpy as np


class ImageClassifier:
    def __init__(self, model_path: str) -> None:
        self.model_path = model_path
        self.model = self._load_model()

    def _check_model(self) -> bool:
        onnx_model = onnx.load(self.model_path)
        try:
            onnx.checker.check_model(onnx_model, True)
            return True
        except Exception:
            return False

    def _load_model(self) -> ort.InferenceSession:
        if not self._check_model():
            raise Exception("Invalid ONNX model")
        return ort.InferenceSession(self.model_path)
    
    def predict(self, image: np.ndarray) -> np.ndarray:
        return self.model.run(None, {"input": image})
    