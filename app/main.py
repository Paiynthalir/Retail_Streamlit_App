# Streamlit APP to consume the APIs hosted at https://retail-fastapi-app.onrender.com 
# This app is used for
 # 1. Predict the sales revenue for a given item in a specific store at a given date.
 # 2. Forecast the total sales revenue across all stores and items for the next 7 days

# Import packages
import streamlit as st
import pandas as pd
import altair as alt
import datetime

# Import custom functions
from forecast import get_forecasted_sales
from predict import get_predicted_sales, is_valid_store_id, is_valid_item_id

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Sales Prediction and Forecast",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)


# Streamlit application layout
st.title("Sales Prediction and Forecasting")

# Create tabs
tab1, tab2 = st.tabs(["Predict","Forecast"])

# Predict tab
with tab1:
    st.write("Enter the details below to get the predicted sales.")

    # Input fields for the user
    predict_date = st.date_input("Select a date", value=datetime.date.today(),key="predict_date")
    store_id = st.text_input("Enter Store ID", value="CA_1",key="store_id")
    item_id = st.text_input("Enter Item ID", value="HOBBIES_1_006",key="item_id")

    # Button to get the predicted sales
    if st.button("Get Predicted Sales"):
        if predict_date is not None:
            formatted_date = predict_date.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
            
            # Validate store_id
            if not is_valid_store_id(store_id):
                st.warning("Store ID must be in the format 'TX_<digit>', 'CA_<digit>', or 'WI_<digit>'.")
            elif not is_valid_item_id(item_id):
                st.warning("Item ID must be in the format '<category>_<digit>_<3 digits>' where category is HOUSEHOLD, HOBBIES, or FOODS.")
            else:
                # Call the function to get predicted sales
                prediction_data = get_predicted_sales(formatted_date, store_id, item_id)

                # Display the result
                if prediction_data:
                    st.subheader("Predicted Sales:")
                    st.markdown(f"The predicted sales of **{item_id}** in **{store_id}** is <span style='color:red; font-weight:bold;'>${prediction_data['prediction']:.2f}</span>.", unsafe_allow_html=True)

        else:
            st.warning("Please select a valid date.")

# Forecast tab
with tab2:
    st.markdown("## Sales Forecasting")
    st.write("Please select a date to get the forecasted sales across all stores and items for the next 7 days.")
    
    # Input for the date
    forecast_date = st.date_input("Select a date", value=datetime.date.today(),key="forecast_date")

    # Button to get the forecast
    if st.button("Get Forecast"):
        if forecast_date is not None:
            # Format date as YYYY-MM-DD
            formatted_date = forecast_date.strftime("%Y-%m-%d")
            # Call the function to get forecasted sales
            forecast_data = get_forecasted_sales(formatted_date)

            # Display the results
            if forecast_data:
                st.subheader("Forecasted Sales for the Next 7 Days:")
                # Convert the forecast data to a DataFrame
                forecast_df = pd.DataFrame(list(forecast_data.items()), columns=["Date", "Forecasted Sales ($)"])
                # Format the 'Forecasted Sales' column to two decimal places
                forecast_df["Forecasted Sales ($)"] = forecast_df["Forecasted Sales ($)"].map("${:,.2f}".format)

                # Display the DataFrame as a table
                st.table(forecast_df)
        else:
            st.warning("Please select a valid date.")