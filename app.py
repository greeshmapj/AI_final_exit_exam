import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image

model = tf.keras.models.load_model(
    "models/intel_mobilenet.h5"
)

classes = [
    'buildings',
    'forest',
    'glacier',
    'mountain',
    'sea',
    'street'
]

def predict_image(img):

    img = img.convert("RGB")

    img = img.resize((150,150))

    img = np.array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    class_idx = np.argmax(prediction)

    confidence = np.max(prediction)

    return classes[class_idx], confidence

st.title("Intel Scene Classifier")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=['jpg','png','jpeg']
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image)

    result = predict_image(image)

    st.success(
        f"Predicted Class: {result}"
    )