import streamlit as st
import requests
import re

# Function to call the FastAPI endpoint
def get_predicted_sales(date: str, store_id: str, item_id: str):
    """
    Call the FastAPI endpoint to get the predicted sales for a specific item in a store.

    Args:
        date (str): The date for which to predict sales (format: YYYY-MM-DD).
        store_id (str): The identifier of the store.
        item_id (str): The identifier of the item.

    Returns:
        dict: A dictionary containing the predicted sales.
    """
    # Construct the URL with query parameters
    url = f"https://retail-fastapi-app.onrender.com/sales/stores/items/?date={date}&store_id={store_id}&item_id={item_id}"

    try:
        # Make the GET request to the FastAPI endpoint
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Return the JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    

# Function to validate the store ID
def is_valid_store_id(store_id: str) -> bool:
    pattern = r'^(TX|CA|WI)_[0-9]$'  # Regex for TX_<single digit>, CA_<single digit>, WI_<single digit>
    return re.match(pattern, store_id) is not None


# Function to validate the item ID
def is_valid_item_id(item_id: str) -> bool:
    pattern = r'^(HOUSEHOLD|HOBBIES|FOODS)_[0-9]_[0-9]{3}$'  # Regex for <category>_<single digit>_<3 digits>
    return re.match(pattern, item_id) is not None