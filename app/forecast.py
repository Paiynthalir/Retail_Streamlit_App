# import packages
import streamlit as st
import requests
import json

# Function to call the FastAPI endpoint and 
# return the json formated output with date:forecasted sales revenue as key value pairs
def get_forecasted_sales(date):
    url = f"https://retail-fastapi-app.onrender.com/sales/national/?date={date}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
    return None