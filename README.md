﻿# Retail_Streamlit_App
This app is used for
  1. Predict the sales revenue for a given item in a specific store at a given date.
  2. Forecast the total sales revenue across all stores and items for the next 7 days

## Backend details:
This streamlit app consumes the following APIs(sample input parameters provided) which has been hosted through a docker image using render (docker.io/paiynthalir/retail_fastapi_app:latest)
1. https://retail-fastapi-app.onrender.com/
2. https://retail-fastapi-app.onrender.com/health
3. https://retail-fastapi-app.onrender.com/sales/stores/items/?item_id=HOBBIES_1_006&store_id=CA_1&date=2016-10-01
4. https://retail-fastapi-app.onrender.com/sales/national/?date=2016-10-01

## Steps to build the docker container and test locally
Test streamlit docker file locally
1. To bulild docker image
    - docker build -t retail_streamlit_app .
2. To create docker container
    - docker run --rm -p 8501:8501 retail_streamlit_app
3. To test locally
    - http://localhost:8501

## Push the docker container to hub
1. Single command to build the docker container that supports multiple platforms and push to docker hub
    - docker buildx build --platform linux/amd64,linux/arm64 -t paiynthalir/retail_streamlit_app:latest --push .

## Steps to deploy in render
Deploy to Render so as to make the app accessible to public
1. Log into your Render account
2. On Render create a new Web Service
3. Connect to your Github account and provide access to the adv_mla_lab_4_app repo
4. Select Existing Image for the Source Code
5. Paste your image URL: docker.io/paiynthalir/retail_streamlit_app
6. Select the Free Tier
7. Click on Deploy Service and it will take few minutes for Render to deploy the app (around 10 min)
8. Access the streamlit app @ https://retail-streamlit-app.onrender.com

