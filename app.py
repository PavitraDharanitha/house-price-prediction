import streamlit as st
import pickle
import numpy as np

# Load model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("House Price Prediction App")

st.write("Enter house details below")

# Inputs
area = st.number_input("Area (sq ft)", min_value=0)

bedrooms = st.number_input("Bedrooms", min_value=0)

bathrooms = st.number_input("Bathrooms", min_value=0)

stories = st.number_input("Stories", min_value=0)

parking = st.number_input("Parking", min_value=0)

if st.button("Predict Price"):

    features = np.array([[area, bedrooms, bathrooms, stories, parking]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")