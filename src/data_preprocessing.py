# src/data_preprocessing.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

from yahoo_fin import stock_info as si

def load_data(ticker, start_date, end_date):
    """
    Fetch historical stock data
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker} between {start_date} and {end_date}.")

    # Fetch P/E ratio
    pe_ratio = si.get_stats_valuation(ticker)
    pe_ratio = pe_ratio[pe_ratio.iloc[:, 0] == 'Trailing P/E'].iloc[0, 1]
    pe_ratio = float(pe_ratio)

    data['PE_Ratio'] = pe_ratio

    return data


def preprocess_data(data):
    """
    Preprocess and scale the data.
    """
    features = data[['Close', 'PE_Ratio']].copy()

    features['PE_Ratio'].fillna(method='ffill', inplace=True)
    features['PE_Ratio'].fillna(method='bfill', inplace=True)

    if features.isnull().values.any():
        raise ValueError("NaN values found in features after filling missing values.")

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(features)

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

    return X_train, y_train, X_test, y_test

def create_sequences(dataset, time_step):
    """
    Create sequences of data for input.
    """
    X, y = [], []
    for i in range(len(dataset) - time_step):
        X.append(dataset[i:i + time_step])
        y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(y)

def load_and_preprocess_data(ticker, start_date, end_date):
    """
    Load and preprocess.
    """
    data = load_data(ticker, start_date, end_date)
    scaled_data, scaler = preprocess_data(data)
    X_train, y_train, X_test, y_test = create_datasets(scaled_data)
    return X_train, y_train, X_test, y_test, scaler, data
