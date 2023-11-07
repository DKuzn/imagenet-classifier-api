import os
import sys

from api.image_processing import ImageProcessing

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_image_decode():
    test_base64 = open("./tests/test_files/test_base64.txt", 'r').read()
    
    image = ImageProcessing.decode_base64(test_base64)
    assert image.shape == (257, 300, 3)
