# 🏠 Nigeria House Price Prediction

## 📌 Overview
This project predicts house prices across Nigeria using machine learning models.  
It leverages a cleaned dataset of over **11,000 property listings** across **23 states** and **185 towns**, with features such as:

- Bedrooms  
- Bathrooms  
- Toilets  
- Parking spaces  
- Property type  
- Town  
- State  

The goal is to provide an interactive tool for estimating property values and exploring housing trends in Nigeria.

---

## 📂 Project Files
- **Nigeria House Price Prediction.pdf** → Full project report with data exploration, cleaning, modeling, and evaluation.  
- **nigeria_houses_data.csv** → Raw dataset containing property listings.  
- **nigeria_houses_data_clean.csv** → Cleaned dataset after removing duplicates, renaming columns, and handling outliers.  
- **house_price_model.pkl** → Saved trained pipeline (XGBoost model).  
- **app.py** → Streamlit app for interactive price prediction.  

---

## 🧹 Data Cleaning
Steps performed:
- Removed **10,438 duplicate entries**.  
- Renamed `title` → `property_type`.  
- Created a new feature:  
  ```python
  total_rooms = bedrooms + bathrooms + toilets + parking_space

---

## 🚀 Features
- Data cleaning and preprocessing pipeline
- Exploratory data analysis (EDA)
- Supervised machine learning model training
- Model evaluation and performance comparison
- House price prediction mini app
- Model serialization for deployment

---

## 🧠 Machine Learning Workflow
1. Data collection and loading
2. Data preprocessing and feature engineering
3. Exploratory data analysis
4. Model training
5. Model evaluation
6. Prediction interface

---

## Model Deployment
[House Price Prediction]{https://nigeria-house-price-prediction-ml-jpxsw4itvhqhnzqmruakbs.streamlit.app/}
