import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
import urllib.request

# Load the trained model and scaler
# model = joblib.load('house_price_model.pkl')  # Replace with the actual path to your model

# Helper function to download model from GitHub
def download_model(url, model_path):
    if not os.path.exists(model_path):
        with st.spinner("Downloading model..."):
            urllib.request.urlretrieve(url, model_path)
        st.success("Model downloaded successfully!")

# Define the GitHub URL for the model
MODEL_URL = "https://github.com/OTDavid9/DATA-SCIENCE---HANDS-ON-PROJECT/raw/main"  # Replace with actual URL
MODEL_PATH = "House Price Prediction/house_price_model.pkl"

# Ensure the model is downloaded
download_model(MODEL_URL, MODEL_PATH)

# Load the trained model
try:
    model = joblib.load(MODEL_PATH)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error("Error loading the model. Please check the file path or format.")
    st.stop()
# Streamlit App
st.title("🏠 House Price Prediction App")

st.write("""
This app demonstrates house price prediction based on input features.  
Enter the details below to see the predicted price!
""")

# User inputs
area = st.number_input("Area (sq ft):", min_value=250, max_value=5000, step=1, value=250, format="%d")  # Integer
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=50,step=1, value=1,format="%d")  # Integer
bathrooms = st.number_input("Number of Bathrooms:", min_value=1, max_value=20, value=1, format="%d")  # Integer
house_age = st.number_input("House Age:", min_value=0, max_value=100, step=1, value=0, format="%d")  # Integer
lot_size = st.number_input("Lot Size (acres):", min_value=0.0, max_value=10.0, step=0.1, value=0.5)  # Float
garage = st.selectbox("Garage Size (Number of Cars):", [0, 1, 2, 3, 4])  # Integer
neighborhood_quality = st.slider("Neighborhood Quality (1-10):", min_value=1, max_value=10, value=0)  # Integer

# Prepare data for prediction

new_data = pd.DataFrame({
    'Square_Footage': [area],
    'Num_Bedrooms': [bedrooms],
    'Num_Bathrooms': [bathrooms],
    'House_Age': [house_age],
    'Lot_Size': [lot_size],
    'Garage_Size': [garage],
    'Neighborhood_Quality': [neighborhood_quality]
})

# Predict button
if st.button("Predict"):
    # Make a prediction
    predicted_price = model.predict(new_data)  # Predicting using the trained model
    
    # Convert NumPy array to a native Python float
    predicted_price = predicted_price[0]  # Extract the first element if it's a single prediction
    
    st.success(f"Predicted House Price: ${predicted_price:,.2f}")
    print(f"Predicted House Price: ${predicted_price:,.2f}")

st.write("""
---  
Built with ❤️ using Streamlit.
""")
