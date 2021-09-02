FROM python:3.9
WORKDIR /code
RUN apt-get update && apt-get install -y python3-opencv
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY / .
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "obtect.api:app" ]
