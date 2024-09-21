# src/data_preprocessing.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

def load_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker} between {start_date} and {end_date}.")
    return data

def preprocess_data(data):
    """
    Preprocess the data by selecting the 'Close' price and scaling it.
    """
    closing_prices = data[['Close']]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(closing_prices)
    return scaled_data, scaler

def create_datasets(scaled_data, time_step=60, train_split=0.8):
    """
    Create training and testing datasets.
    """
    training_size = int(len(scaled_data) * train_split)
    train_data = scaled_data[:training_size]
    test_data = scaled_data[training_size:]

    X_train, y_train = create_sequences(train_data, time_step)
    X_test, y_test = create_sequences(test_data, time_step)

    # Reshape input to be [samples, time steps, features] which is required for LSTM
    X_train = X_train.reshape(-1, time_step, 1)
    X_test = X_test.reshape(-1, time_step, 1)

    return X_train, y_train, X_test, y_test

def create_sequences(dataset, time_step):
    """
    Create sequences of data for LSTM input.
    """
    X, y = [], []
    for i in range(len(dataset) - time_step):
        X.append(dataset[i:i + time_step, 0])
        y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(y)

def load_and_preprocess_data(ticker, start_date, end_date):
    """
    Orchestrates the loading and preprocessing of data.
    """
    data = load_data(ticker, start_date, end_date)
    scaled_data, scaler = preprocess_data(data)
    X_train, y_train, X_test, y_test = create_datasets(scaled_data)
    return X_train, y_train, X_test, y_test, scaler, data
