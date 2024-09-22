# src/prediction.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def make_future_predictions(model, data, scaler, time_step=60, days_ahead=30):
    """
    Predict future stock prices for the next 'days_ahead' days.
    """
    # Prepare initial input data
    last_data = data[['Close', 'PE_Ratio']].values[-time_step:]
    temp_input = list(last_data)

    future_predictions = []

    for _ in range(days_ahead):
        # Prepare the input sequence
        input_seq = np.array(temp_input[-time_step:])
        input_seq_scaled = scaler.transform(input_seq)
        input_seq_scaled = input_seq_scaled.reshape(1, time_step, input_seq.shape[1])

        # Make prediction
        pred = model.predict(input_seq_scaled)
        pred_value = pred[0][0]

        # Inverse transform the predicted value
        pred_full = np.array([[pred_value, 0]])  # Placeholder for 'PE_Ratio'
        pred_inverse = scaler.inverse_transform(pred_full)
        pred_price = pred_inverse[0][0]
        future_predictions.append(pred_price)

        # Update temp_input with the new predicted value
        # Assume P/E ratio remains the same as the last known value
        last_pe_ratio = temp_input[-1][1]
        temp_input.append([pred_price, last_pe_ratio])

    return future_predictions

def plot_future_predictions(future_predictions, data, ticker):
    """
    Plot and save the predicted future prices along with historical data.
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

    # Save the plot
    if not os.path.exists('data'):
        os.makedirs('data')
    plot_path = os.path.join('data', f'{ticker}_future_prediction.png')
    plt.savefig(plot_path)
    plt.close()