import io
import numpy as np
import PIL.Image
import tensorflow as tf

from PIL import Image, ImageOps
from PIL import Image
from fastapi import FastAPI, File, UploadFile, Response

# Load the trained TensorFlow model
model = tf.keras.models.load_model('./supported_model/mnist_model.h5')

app = FastAPI()

@app.get("/liveness")
async def liveness_probe(response: Response):
    response.status_code = 200
    return {"status": "alive"}

@app.get("/readiness")
async def readiness_probe(response: Response):
    response.status_code = 200
    return {"status": "ready"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()
    image = PIL.Image.open(io.BytesIO(contents))
    image = image.convert("L")
    image_inverted = image.resize((28, 28))
    img_array = np.array(image_inverted)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # shape = (1, 28, 28)

    predictions = model.predict(img_array)
    print(predictions)
    predicted_class = np.argmax(predictions, axis=1)[0]
    return {"predicted_class": int(predicted_class)}