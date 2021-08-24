import torch


class Model:

    def __init__(self):
        self._model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def predict_and_render(self, img):
        predict = self._model(img)
        rendered_img = predict.render()[0]
        return rendered_img
