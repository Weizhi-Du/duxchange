# app.py

from flask import Flask, send_from_directory, jsonify
import os
import pandas as pd

app = Flask(__name__, static_folder='frontend/build', static_url_path='')

DATA_DIR = 'data'

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/predictions/<ticker>')
def get_predictions(ticker):
    """
    Serve prediction data and images for a given ticker symbol.
    """
    try:
        # Load future predictions CSV
        csv_path = os.path.join(DATA_DIR, f'{ticker}_future_predictions.csv')
        if not os.path.exists(csv_path):
            return jsonify({'error': 'Prediction data not found.'}), 404

        predictions_df = pd.read_csv(csv_path)
        predictions = predictions_df.to_dict(orient='records')

        return jsonify({'predictions': predictions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/plots/<ticker>/<plot_type>')
def get_plot(ticker, plot_type):
    """
    Serve plot images for a given ticker symbol.
    """
    try:
        filename = f'{ticker}_{plot_type}.png'
        file_path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(file_path):
            return jsonify({'error': 'Plot not found.'}), 404
        return send_from_directory(DATA_DIR, filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
