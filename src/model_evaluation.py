# src/model_evaluation.py

import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test, scaler):
    """
    Evaluate the model's performance on the test set.
    """
    predictions = model.predict(X_test)
    # Since only 'Close' was scaled, we need to inverse transform accordingly
    y_test_scaled = scaler.inverse_transform(np.concatenate([y_test.reshape(-1, 1), np.zeros((len(y_test), 1))], axis=1))[:, 0]
    predictions_scaled = scaler.inverse_transform(np.concatenate([predictions, np.zeros((len(predictions), 1))], axis=1))[:, 0]

    rmse = np.sqrt(mean_squared_error(y_test_scaled, predictions_scaled))
    print(f"Test RMSE: {rmse:.2f}")

    return predictions_scaled, y_test_scaled

def plot_results(y_true, y_pred, ticker):
    """
    Plot the actual vs predicted stock prices.
    """
    plt.figure(figsize=(14, 5))
    plt.plot(y_true, label='Actual Stock Price')
    plt.plot(y_pred, label='Predicted Stock Price')
    plt.title(f'{ticker} Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
