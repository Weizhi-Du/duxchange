# Duxchange - A Stock Price Predictor

This repository serves as my submission to the WUCG Hackathon at WashU. It's a project that predicts stock prices using a Long Short-Term Memory (LSTM) neural network. 

## Division

Advanced Group

Video demo: ./demo/Demo.mp4

## Team Members

**Weizhi Du**
- Sophomore
- Computer Science & Financial Engineering
- I did everything. It's all on me :)

[![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/duw)

## Features

- Fetches historical stock data using Yahoo Finance API.
- Preprocesses data for training.
- Trains an LSTM model, a recurrent neural network (RNN), for prediction.
- Visualizes actual vs. predicted stock prices.

## Technical Stack

- Python, Tensorflow, Keras, Scikit-learn, ReactJS, Flask, Numpy, Pandas, Matplotlib

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/weizhi-du/duxchange.git

2. **Enter the repository:**

   ```bash
   cd duxchange
   
3. **Set up virtual environment:**

   ```bash
   sudo pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   
4. **Install required packages:**

   ```bash
   pip install -r requirements.txt

5. **Example command-line Usage:**

   ```bash
   python src/main.py --ticker MS --start_date 2010-01-01 --end_date 2024-09-20 --days_ahead 10

6. **Open with Web UI:**

   ```bash
   python app.py
   
This program will be hosted at https://127.0.0.1:5000/

## Special Thanks

My liver. Literally spent 5 hours on sleeping and the rest all on this project. I would feel guilty if I have a teammate :)


![GitHub last commit](https://img.shields.io/github/last-commit/weizhi-du/duxchange)
![GitHub license](https://img.shields.io/github/license/weizhi-du/duxchange)
