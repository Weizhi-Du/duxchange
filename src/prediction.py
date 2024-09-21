# src/prediction.py

import numpy as np
import matplotlib.pyplot as plt

def make_predictions(model, data, scaler, time_step=60):
    """
    Make future stock price predictions.
    """
    last_data = data[-time_step:]
    input_data = last_data.reshape(1, -1)
    input_data = scaler.transform(input_data.T)

    X_input = input_data.reshape(1, time_step, 1)
    prediction = model.predict(X_input)
    prediction = scaler.inverse_transform(prediction)

    return prediction[0][0]

def plot_future_prediction(prediction, data, ticker):
    """
    Plot the predicted future price along with historical data.
    """
    plt.figure(figsize=(14, 5))
    plt.plot(data['Close'], label='Historical Stock Price')
    plt.scatter(len(data), prediction, color='red', label='Predicted Stock Price')
    plt.title(f'{ticker} Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
