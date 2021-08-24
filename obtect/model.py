import torch
from PIL import Image


class Model:
    """Class for utilizig yolov5 model"""

    def __init__(self):
        self._model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def predict_and_render(self, img: Image) -> Image:
        """Detect objects using yolov5 model

        Parameters
        ----------
        img : Image
            Input image whose objects are going to be detected.

        Returns
        -------
        rendered_img : Image
            Rendered image with detected objects. They are shown with
            a rectangle around the object with their name and
            confidence level.
        """
        predict = self._model(img)  # feed the image into model
        rendered_img = predict.render()[0]  # rendered image from model output
        rendered_img = Image.fromarray(rendered_img)
        return rendered_img
