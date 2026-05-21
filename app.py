import streamlit as st
import pickle
import numpy as np

# Load model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter number of rooms")

# Input
rooms = st.number_input("Rooms", min_value=1)

# Prediction
if st.button("Predict Price"):

    features = np.array([[rooms]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
