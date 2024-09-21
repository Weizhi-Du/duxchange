# src/model_evaluation.py

import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test, scaler):
    """
    Evaluate the model's performance on the test set.
    """
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions.reshape(-1, 1))
    y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))

    rmse = np.sqrt(mean_squared_error(y_test_scaled, predictions))
    print(f"Test RMSE: {rmse:.2f}")

    return predictions, y_test_scaled

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
