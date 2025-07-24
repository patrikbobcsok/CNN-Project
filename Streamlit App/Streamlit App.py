import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import json
from tensorflow.keras.applications.vgg16 import preprocess_input

# Load VGG16 fine-tuned model
model = tf.keras.models.load_model("/Users/patrikbobcsok/Desktop/Ironhack/Deep Learning - Image Classification with CNN Project/CNN_Image_Classifier_VGG16/cnn_animals10_VGG16_finetuned.h5")

# Load class names
with open("class_names.json", "r") as f:
    class_names = json.load(f)

st.title("🐾 Animal Image Classifier")
st.write("Upload an animal image, and the model will predict its class!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Decode image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # BGR
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display image
    st.image(image_rgb, caption="Uploaded Image", use_container_width=True)

    # Preprocess for VGG16
    img_resized = cv2.resize(image_rgb, (160, 160))
    img_preprocessed = preprocess_input(img_resized)
    img_batch = np.expand_dims(img_preprocessed, axis=0)

    # Predict
    predictions = model.predict(img_batch)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions)

    st.subheader("Prediction:")
    st.write(f"**{predicted_class}** ({confidence * 100:.2f}% confidence)")