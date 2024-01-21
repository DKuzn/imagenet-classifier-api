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


def test_image_resize():
    test_base64 = open("./tests/test_files/test_base64.txt", 'r').read()
    
    image = ImageProcessing.decode_base64(test_base64)
    resize_smaller = ImageProcessing.resize(image, (224, 224))
    resize_bigger = ImageProcessing.resize(image, (512, 512))
    assert resize_smaller.shape == (224, 224, 3)
    assert resize_bigger.shape == (512, 512, 3)