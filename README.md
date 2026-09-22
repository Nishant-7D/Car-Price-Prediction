# Car Price Prediction

A Machine Learning web application that predicts the resale price of a used car based on features such as brand, car model, year, fuel type, seller type, transmission, owner history, engine, mileage, and maximum power.

The project uses a **Random Forest Regression** model and provides an interactive interface built with **Streamlit**.

# live demo
(https://car-price-prediction-fast.streamlit.app/)

# Project Overview

Buying or selling a used car can be difficult because prices depend on many factors.

This project uses historical car data to train a Machine Learning model that estimates the expected price of a car based on its specifications.

The trained model is integrated into a Streamlit web application where users can enter car details and instantly receive a predicted price.

# Features

*  Used car price prediction
*  Random Forest Regression model
*  Data preprocessing and feature engineering
*  Brand and car-model based prediction
*  Fuel type selection
*  Manual/Automatic transmission selection
*  Seller and ownership information
*  Car age calculation
*  Interactive Streamlit web application
*  Instant prediction

# Machine Learning Model

The project uses:

**Random Forest Regressor**

The dataset was cleaned and processed before training.

# Important Features

Some of the most influential features in the trained model were:

* Maximum Power
* Car Age
* Car Model
* Year
* Engine
* Mileage
* Fuel Type

Feature importance analysis showed that **maximum power and car age** were among the major contributors to the model's predictions.

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn
* Google Colab
* Pickle

# Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── model.pkl
├── Cardetails.csv
├── car_price_prediction.ipynb
├── requirements.txt
└── README.md
```

# How It Works

```text
Car Details
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
Random Forest Model
     ↓
Predicted Car Price
```

The user enters the required vehicle information through the Streamlit interface. The application processes the inputs and passes them to the trained Machine Learning model to generate an estimated resale price.

# Dataset

The project uses a used-car dataset containing information about different vehicles and their selling prices.

Important columns include:

* Brand
* Car Model
* Year
* Selling Price
* KM Driven
* Fuel
* Seller Type
* Transmission
* Owner
* Mileage
* Engine
* Max Power
* Seats

# Future Improvements

* Add more recent car-price data
* Compare multiple regression algorithms
* Improve model accuracy through hyperparameter tuning
* Add interactive data visualizations
* Deploy the application online
* Add more advanced feature engineering
* Add explainable AI features to show why a particular price was predicted

Interested in Machine Learning, Data Analytics, Python, SQL and AI.

 If you find this project useful, consider giving the repository a star!
