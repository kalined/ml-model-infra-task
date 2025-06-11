import io
import numpy as np
import PIL.Image
import tensorflow as tf

from PIL import Image, ImageOps
from PIL import Image
from fastapi import FastAPI, File, UploadFile

# Load the trained TensorFlow model
model = tf.keras.models.load_model('./supported_model/mnist_model.h5')

app = FastAPI()

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
    predicted_class = np.argmax(predictions, axis=1)[0]
    return {int(predicted_class)}