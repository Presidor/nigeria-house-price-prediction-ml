import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# APP CONFIG
# -------------------------------
st.set_page_config(
    page_title="Nigeria House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Nigeria House Price Prediction App")
st.write("Predict house prices using machine learning based on property features.")

# -------------------------------
# FILE PATH SETUP (PRODUCTION SAFE)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "house_price_model.pkl")
data_path = os.path.join(BASE_DIR, "nigeria_houses_data_clean.csv")

# -------------------------------
# LOAD MODEL + DATA (CACHED)
# -------------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

@st.cache_data
def load_data():
    try:
        return pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        st.stop()

model = load_model()
df = load_data()

# -------------------------------
# SIDEBAR INPUTS
# -------------------------------
st.sidebar.header("🏡 Property Details")

bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 3)
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, 2)
toilets = st.sidebar.slider("Toilets", 1, 10, 2)
parking_space = st.sidebar.slider("Parking Space", 0, 10, 1)

# Location inputs
state = st.sidebar.selectbox("State", sorted(df["state"].unique()))

filtered_towns = df[df["state"] == state]["town"].unique()
town = st.sidebar.selectbox("Town", sorted(filtered_towns))

property_type = st.sidebar.selectbox(
    "Property Type",
    sorted(df["property_type"].unique())
)

# -------------------------------
# FEATURE ENGINEERING
# -------------------------------
total_rooms = bedrooms + bathrooms + toilets + parking_space

# -------------------------------
# PREDICTION
# -------------------------------
if st.sidebar.button("Predict Price"):

    try:
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

        st.success(f"💰 Estimated House Price: ₦{prediction:,.0f}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Machine Learning House Price Prediction System")




