# src/model_evaluation.py

import os
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test, scaler, ticker):
    """
    Evaluate the model's performance on the test set.
    """
    predictions = model.predict(X_test)
    # Inverse transform predictions
    y_test_scaled = scaler.inverse_transform(
        np.concatenate([y_test.reshape(-1, 1), np.zeros((len(y_test), scaler.n_features_in_ - 1))], axis=1)
    )[:, 0]
    predictions_scaled = scaler.inverse_transform(
        np.concatenate([predictions, np.zeros((len(predictions), scaler.n_features_in_ - 1))], axis=1)
    )[:, 0]

    rmse = np.sqrt(mean_squared_error(y_test_scaled, predictions_scaled))
    print(f"Test RMSE: {rmse:.2f}")

    return predictions_scaled, y_test_scaled

def plot_results(y_true, y_pred, ticker):
    """
    Plot and save the actual vs predicted stock prices.
    """
    plt.figure(figsize=(14, 5))
    plt.plot(y_true, label='Actual Stock Price')
    plt.plot(y_pred, label='Predicted Stock Price')
    plt.title(f'{ticker} Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()

    # Save the plot
    if not os.path.exists('data'):
        os.makedirs('data')
    plot_path = os.path.join('data', f'{ticker}_prediction.png')
    plt.savefig(plot_path)
    plt.close()
