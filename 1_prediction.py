import numpy as np
import pandas as pd
import streamlit as st
import pickle

model = pickle.load(open("iris_model.pkl", "rb"))

st.title("Iris Flower Prediction")

sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 1.0)

predict = st.button("Predict Species")

if predict:
    data = np.array([[sepal_length, sepal_width,
                      petal_length, petal_width]])

    prediction = model.predict(data)

    st.success("Predicted Species: " + str(prediction[0]))