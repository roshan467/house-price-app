import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("🏡 House Price Prediction App")
st.write("Enter the details below to predict house price")

# Input fields for numerical features
longitude = st.number_input("Longitude", value=-119.01)
latitude = st.number_input("Latitude", value=36.06)
housing_median_age = st.number_input("Housing Median Age", value=25.0)
total_rooms = st.number_input("Total Rooms", value=1505.0)
total_bedrooms = st.number_input("Total Bedrooms", value=435.0)
population = st.number_input("Population", value=1392.0)
households = st.number_input("Households", value=359.0)
median_income = st.number_input("Median Income", value=1.6812)

# Input for categorical feature (ocean proximity)
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
)

# Encode categorical input (one-hot encoding manually)
ocean_features = [
    1 if ocean_proximity == "INLAND" else 0,
    1 if ocean_proximity == "ISLAND" else 0,
    1 if ocean_proximity == "NEAR BAY" else 0,
    1 if ocean_proximity == "NEAR OCEAN" else 0,
]

# Prepare input for model
features = np.array([[longitude, latitude, housing_median_age, total_rooms,
                      total_bedrooms, population, households, median_income] + ocean_features])

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(features)[0]
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")
