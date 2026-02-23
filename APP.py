import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("house_price_model.pkl")

# Load dataset for dropdowns
df = pd.read_csv("nigeria_houses_data.csv")

# Sidebar inputs
st.sidebar.header("House Features")
bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 3)
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, 3)
toilets = st.sidebar.slider("Toilets", 1, 10, 3)
parking_space = st.sidebar.slider("Parking Space", 0, 10, 2)

state = st.sidebar.selectbox("State", df["state"].unique())
town = st.sidebar.selectbox("Town", df["town"].unique())
property_type = st.sidebar.selectbox("Property Type", df["property_type"].unique())

# Compute total rooms
total_rooms = bedrooms + bathrooms + toilets + parking_space

# Predict button
if st.sidebar.button("Predict Price"):
    features = pd.DataFrame([{
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "toilets": toilets,
        "parking_space": parking_space,
        "total_rooms": total_rooms,
        "property_type": property_type,
        "town": town,
        "state": state
    }])
    prediction = model.predict(features)[0]
    st.success(f"Estimated House Price: ₦{prediction:,.0f}")
