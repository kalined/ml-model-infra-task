FROM python:3.11-slim

WORKDIR /app

COPY src/main.py /app/main.py

COPY supported_model/mnist_model.h5 /app/supported_model/mnist_model.h5

RUN pip install --no-cache-dir fastapi python-multipart uvicorn tensorflow pillow numpy

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]