# src/model_training.py

from keras.models import Sequential
from keras.layers import LSTM, Dense
import os

def build_model(input_shape):
    """
    Build an LSTM model that accepts multiple features.
    """
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))  # Output layer predicts the 'Close' price
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(X_train, y_train, X_val=None, y_val=None, epochs=20, batch_size=32):
    """
    Train the LSTM model.
    """
    model = build_model((X_train.shape[1], X_train.shape[2]))
    if X_val is not None and y_val is not None:
        history = model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            verbose=1
        )
    else:
        history = model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            verbose=1
        )
    return model, history

def save_model(model, model_name='lstm_model.h5'):
    """
    Save the trained model to disk.
    """
    if not os.path.exists('models'):
        os.makedirs('models')
    model.save(os.path.join('models', model_name))
