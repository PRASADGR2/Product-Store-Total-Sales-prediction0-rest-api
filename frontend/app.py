
import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# Base URL of the Flask backend
Backend_URL = "http://backend:7860"

st.title("SuperKart Total Sales Predictor") # define the title of the app.
st.write("This tool predicts the Product Store Sales Total")

# Input fields for product and store data
Product_Id = st.text_input("Product_Id") # define the UI element for Product_Id
Product_Weight = st.number_input("Product Weight (Number)", min_value=0.0, value=12.66) # define the UI element for Product_Weight
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"]) # define the UI element for Product_Sugar_Content
Product_Allocated_Area = st.number_input("Product Allocated Area (Number)") # define the UI element for Product_Allocated_Area
Product_Type_Category = st.selectbox("Product Type", ["Baking Goods", "Breads", "Breakfast", "Canned", "Dairy", "Frozen Foods", "Fruits and Vegetables", "Hard Drinks", "Health and Hygiene", "Household", "Meat", "Others", "Seafood", "Snack Foods", "Soft Drinks", "Starchy Foods"]) # define the UI element for Product_Type_Category
Product_MRP = st.number_input("Product MRP (Number)") # define the UI element for Product_MRP
Store_Id = st.selectbox("Store Id", ["OUT001", "OUT002", "OUT003", "OUT004"]) # define the UI element for Store_Id
Store_Establishment_year_str = st.selectbox("Store Establishment Year", ["1987", "1998", "1999", "2009"]) # define the UI element for Store_Establishment_year_str
Store_Size = st.selectbox("Store Size", ["High", "Medium", "Small"]) # define the UI element for Store_Size
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"]) # define the UI element for Store_Location_City_Type
Store_Type = st.selectbox("Store Type", ["Departmental Store", "Food Mart", "Supermarket Type1", "Supermarket Type2"]) # define the UI element for Store_Type
Store_Age_Years = datetime.now().year - int(Store_Establishment_year_str)  # define the UI element for Store_Age_Years

st.number_input(
    "Store Age (Years)",
    value=Store_Age_Years,
    disabled=True
)

# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    "Product_Id": Product_Id,
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_Type_Category": Product_Type_Category,
    "Product_MRP": Product_MRP,
    "Store_Id": Store_Id,
    "Store_Establishment_year_str": Store_Establishment_year_str,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Store_Age_Years": Store_Age_Years
}])

# Make prediction when the "Predict" button is clicked

if st.button("Predict", type="primary"):
    response = requests.post(f"{Backend_URL}/v1/predictprodstoresales", json=input_data.to_dict(orient='records')[0])  # Send data to Flask API
    if response.status_code == 200:
        prediction = response.json()["Sales"]
        st.success(f"Predicted Product Store Sales Total: ${prediction:,.2f}")
    else:
        st.error("Error in API request")

# ==========================
# Sidebar Footer
# ==========================

st.sidebar.markdown("---")
st.sidebar.markdown("### Developed by")
st.sidebar.markdown("**Raghavendra Gattamaraju**")
