# Retail_Streamlit_App
This app is used for
  1. Predict the sales revenue for a given item in a specific store at a given date.
  2. Forecast the total sales revenue across all stores and items for the next 7 days

## Backend details:
This streamlit app consumes the following APIs(sample input parameters provided) which has been hosted through a docker image using render (docker.io/paiynthalir/retail_fastapi_app:latest)
https://retail-fastapi-app.onrender.com/
https://retail-fastapi-app.onrender.com/health
https://retail-fastapi-app.onrender.com/sales/stores/items/
https://retail-fastapi-app.onrender.com/sales/stores/items/?item_id=HOBBIES_1_006&store_id=CA_1&date=2016-10-01
https://retail-fastapi-app.onrender.com/sales/national/?date=2016-10-01
