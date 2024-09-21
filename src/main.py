# src/main.py

import argparse
import sys

from data_preprocessing import load_and_preprocess_data
from model_training import train_model, save_model
from model_evaluation import evaluate_model, plot_results
from prediction import make_predictions, plot_future_prediction

def main(ticker, start_date, end_date):
    print(f"Loading and preprocessing data for {ticker} from {start_date} to {end_date}...")
    X_train, y_train, X_test, y_test, scaler, data = load_and_preprocess_data(ticker, start_date, end_date)

    print("Training the model...")
    model, history = train_model(X_train, y_train, X_test, y_test)

    print("Evaluating the model...")
    predictions, y_test_scaled = evaluate_model(model, X_test, y_test, scaler)

    print("Plotting the results...")
    plot_results(y_test_scaled, predictions, ticker)

    print("Saving the model...")
    save_model(model)

    print("Making future predictions...")
    future_prediction = make_predictions(model, data['Close'].values, scaler)
    print(f"Predicted future stock price: {future_prediction:.2f}")

    plot_future_prediction(future_prediction, data, ticker)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stock Price Prediction using LSTM')
    parser.add_argument('--ticker', type=str, required=True, help='Stock ticker symbol (e.g., AAPL)')
    parser.add_argument('--start_date', type=str, required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end_date', type=str, required=True, help='End date in YYYY-MM-DD format')

    args = parser.parse_args()

    try:
        main(args.ticker, args.start_date, args.end_date)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
