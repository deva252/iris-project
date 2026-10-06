import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Iris Flower Visualization")

# Load Iris dataset
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=[
        "Sepal Length",
        "Sepal Width",
        "Petal Length",
        "Petal Width"
    ]
)

df["Species"] = [iris.target_names[i] for i in iris.target
]

st.subheader("Iris Dataset")
st.dataframe(df)

# Bar Chart
st.subheader("Average Measurements by Species")

average = df.groupby("Species").mean()

st.bar_chart(average)

# Scatter Chart
st.subheader("Petal Length vs Petal Width")

st.scatter_chart(
    df,
    x="Petal Length",
    y="Petal Width"
)