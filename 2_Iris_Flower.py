import streamlit as st

st.title("🌸 Iris Flower Details")

st.write("""
The Iris flower is a beautiful flowering plant.
There are three main species in the Iris dataset.
""")

st.header("🌼 1. Iris Setosa")

st.write("""
Iris Setosa has small petals and relatively large sepals.
""")

st.image("image/setosa.jpg", caption="Iris Setosa")


st.header("🌷 2. Iris Versicolor")

st.write("""
Iris Versicolor has medium-sized petals and sepals.
""")

st.image("image/versicolor.jpg", caption="Iris Versicolor")


st.header("🌺 3. Iris Virginica")

st.write("""
Iris Virginica generally has larger petals compared with the other two species.
""")

st.image("image/virginica.jpg", caption="Iris Virginica")


st.header("📏 Important Measurements")

st.write("""
• Sepal Length
• Sepal Width
• Petal Length
• Petal Width
""")