import streamlit as st
import numpy as np
import pickle

# Streamlit App
st.title("🏠 House Price Prediction App")

st.write("""
This app demonstrates house price prediction based on input features.
Type in the details below to see the predicted price!
""")

# User inputs
area = st.number_input("Area (sq ft):", min_value=500, max_value=5000, step=1, value=1000, format="%d")  # Integer
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=10, step=1, value=3, format="%d")  # Integer
bathrooms = st.number_input("Number of Bathrooms:", min_value=1.0, max_value=5.0, step=0.1, value=2.0)  # Float
location = st.selectbox("Location:", ["Urban", "Suburban", "Rural"])  # Categorical
garage = st.selectbox("Garage:", ["Yes", "No"])  # Categorical

# Encode categorical variables
location_mapping = {"Urban": 2, "Suburban": 1, "Rural": 0}
garage_mapping = {"Yes": 1, "No": 0}

# Prepare data for prediction
features = np.array([
    area, 
    bedrooms, 
    bathrooms, 
    location_mapping[location], 
    garage_mapping[garage]
]).reshape(1, -1)

# Predict button
if st.button("Predict"):
    # Use a placeholder prediction formula (replace with your model)
    price = (
        area * 0.5 + 
        bedrooms * 200 + 
        bathrooms * 0.3 + 
        location_mapping[location] * 0.7 + 
        garage_mapping[garage] * 1000 + 
        5000
    )
    st.success(f"Predicted House Price: ${price:,.2f}")

st.write("""
---  
Built with ❤️ using Streamlit.
""")
