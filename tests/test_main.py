import os
import io
import numpy as np
from PIL import Image
from fastapi.testclient import TestClient
import pytest

from .context import app

client = TestClient(app)


@pytest.mark.skip()
def test_two_images(input_filename, target_filename):
    input_image_path = os.path.join(
        os.path.dirname(__file__),
        'test_images',
        input_filename)
    target_image_path = os.path.join(
        os.path.dirname(__file__),
        'test_images',
        target_filename)

    response = client.post(
        '/detect/',
        files={'file': open(input_image_path, 'rb')})

    assert response.status_code == 200

    # Compare two images
    output_image = Image.open(io.BytesIO(response.content))
    output_image = np.array(output_image)
    target_image = Image.open(target_image_path)
    target_image = np.array(target_image)

    np.testing.assert_array_equal(output_image, target_image)


def test_chair_image():
    test_two_images('input_chair.jpeg', 'output_chair.jpeg')


def test_street_mage():
    test_two_images('input_street.jpeg', 'output_street.jpeg')
