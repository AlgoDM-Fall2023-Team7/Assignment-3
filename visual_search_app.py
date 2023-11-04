import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import pickle

st.title("Visual Search Application")

image = st.file_uploader("Upload Your Image for Prediction", type = ['jpg', 'png'])

button_clicked = st.button('Predict', key=1002)
   
if button_clicked:

    st.header("The Image you uploaded")

    st.image(image=image)
        
    img = Image.open(image)
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img)

    img = np.array(img)

    img = img.astype('float32')

    img = np.expand_dims(img, axis = 0)

    model =  tf.keras.models.load_model("ML.h5")

    prediction = model.predict(img)

    Ans_list = ['Dress', 'Hat', 'Long sleeves', 'Shoes', 'T-Shirt']
    st.success(f"The uploaded image is most likely: {Ans_list[np.argmax(prediction)]}")



