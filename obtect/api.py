
from obtect.model import Model

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from PIL import Image
import io

app = FastAPI()
model = Model()


@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    """Detect objects in an image and return rendered image"""
    img = Image.open(io.BytesIO(await file.read()))
    rendered_img = model.predict_and_render(img)

    buffer = io.BytesIO()
    rendered_img.save(buffer, format='JPEG')
    return Response(
        buffer.getvalue(),
        media_type='image/jpeg'
    )
