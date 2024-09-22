# src/prediction.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_future_predictions(model, data, scaler, time_step=60, days_ahead=30):
    """
    Predict future stock prices for the next 'days_ahead' days.

    Parameters:
    - model: Trained LSTM model.
    - data: Original closing prices array.
    - scaler: Fitted MinMaxScaler object.
    - time_step: Number of previous days used for each prediction.
    - days_ahead: Number of future days to predict.

    Returns:
    - future_predictions: Array of predicted prices.
    """
    # Get the last 'time_step' data points
    last_data = data[-time_step:]
    temp_input = list(last_data)

    future_predictions = []

    for _ in range(days_ahead):
        # Prepare the input data
        input_seq = np.array(temp_input[-time_step:])
        input_seq_scaled = scaler.transform(input_seq.reshape(-1, 1))
        input_seq_scaled = input_seq_scaled.reshape(1, time_step, 1)

        # Make prediction
        pred = model.predict(input_seq_scaled)
        pred_value = scaler.inverse_transform(pred)
        future_predictions.append(pred_value[0][0])

        # Append the prediction to the temp_input
        temp_input.append(pred_value[0][0])

    return future_predictions


def plot_future_predictions(future_predictions, data, ticker):
    """
    Plot the predicted future prices along with historical data.

    Parameters:
    - future_predictions: Array of predicted future prices.
    - data: Original DataFrame containing historical data.
    - ticker: Stock ticker symbol.
    """
    last_date = data.index[-1]
    future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=len(future_predictions))

    plt.figure(figsize=(14, 5))
    plt.plot(data['Close'], label='Historical Stock Price')
    plt.plot(future_dates, future_predictions, label='Predicted Future Prices', color='red')
    plt.title(f'{ticker} Stock Price Prediction for Next {len(future_predictions)} Days')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
