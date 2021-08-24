import os
import io
import numpy as np
from PIL import Image
from fastapi.testclient import TestClient

from .context import app

client = TestClient(app)


def test_chair_image():
    input_image_path = os.path.join(
        os.path.dirname(__file__),
        'test_images',
        'input_chair.jpeg')
    target_image_path = os.path.join(
        os.path.dirname(__file__),
        'test_images',
        'output_chair.jpeg')

    response = client.post(
        '/detect/',
        files={'file': open(input_image_path, 'rb')})

    assert response.status_code == 200

    output_image = Image.open(io.BytesIO(response.content))
    output_image = np.array(output_image)
    target_image = Image.open(target_image_path)
    target_image = np.array(target_image)

    np.testing.assert_array_equal(output_image, target_image)
