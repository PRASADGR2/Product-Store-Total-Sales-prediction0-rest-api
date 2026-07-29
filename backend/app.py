
# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API

# Initialize Flask app with a name
superkart_api = Flask("SuperKart Sales Forecast Predictor") # define the name of the app

# Load the trained churn prediction model
model = joblib.load("SuperKart_Model_v1_0.joblib") # define the location of the serialized model
# model = saved_model

# Define a route for the home page
@superkart_api.get('/')
def home():
    return "Welcome to the SuperKart Sales Forecast Prediction API" # define a welcome message

# Define an endpoint to predict churn for a single customer
@superkart_api.post('/v1/predictprodstoresales')
def predict_sales():
    # Get JSON data from the request
    data = request.get_json()

    # Extract relevant customer features from the input data. The order of the column names matters.
    sample = {
        'Product_Id': data['Product_Id'],
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_Type_Category': data['Product_Type_Category'],
        'Product_MRP': data['Product_MRP'],
        'Store_Id': data['Store_Id'],
        'Store_Establishment_year_str': data['Store_Establishment_year_str'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type'],
        'Store_Age_Years': data['Store_Age_Years']
    }

    # Convert the extracted data into a DataFrame
    input_data = pd.DataFrame([sample])

    # Make a churn prediction using the trained model
    prediction = model.predict(input_data).tolist()[0]

    # Return the prediction as a JSON response
    return jsonify({'Sales': prediction})

# Run the Flask app in debug mode
if __name__ == '__main__':
    superkart_api.run(debug=True)
