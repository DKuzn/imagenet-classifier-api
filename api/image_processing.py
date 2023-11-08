import base64
from typing import Tuple

import cv2 as cv
import numpy as np


class ImageProcessing:
    def __init__(self) -> None:
        pass

    @classmethod
    def decode_base64(cls, base64_image: str) -> np.ndarray:
        np_image: np.ndarray = cls._decode_base64(cls, base64_image)
        image = cv.imdecode(np_image, cv.IMREAD_COLOR)
        return cv.cvtColor(image, cv.COLOR_BGR2RGB)

    def _decode_base64(self, base64_image: str) -> np.ndarray:
        byte_image: bytes = base64.b64decode(base64_image)
        return np.frombuffer(byte_image, dtype=np.uint8)
    
    @classmethod
    def resize(cls, image: np.ndarray, size: Tuple(int, int)) -> np.ndarray:
        image_shape = image.shape
        if image_shape[0] > size[0] and image_shape[[1]] > size[1]:
            return cv.resize(image, size, interpolation=cv.INTER_CUBIC)
        
        return cv.resize(image, size, interpolation=cv.INTER_AREA)
