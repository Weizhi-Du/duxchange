# Duxchange - A Stock Price Predictor

This repository serves as my submission to the WUCG Hackathon at WashU. It's a project that predicts stock prices using a Long Short-Term Memory (LSTM) neural network. 

## Division

Advanced Group

## Team Members

**Weizhi Du**
- Sophomore
- Computer Science & Financial Engineering
- It's all on me. I did all the work :)

## Features

- Fetches historical stock data using Yahoo Finance API.
- Preprocesses data for training.
- Trains an LSTM model, a recurrent neural network (RNN), for prediction.
- Visualizes actual vs. predicted stock prices.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/weizhi-du/duxchange.git
   cd duxchange

2. **Clone the repository:**

   ```bash
   git clone https://github.com/weizhi-du/duxchange.git
   cd duxchange
   
3. **Install required packages:**

   ```bash
   pip install -r requirements.txt

4. **Example command-line Usage:**

   ```bash
   python src/main.py --ticker MS --start_date 2010-01-01 --end_date 2024-09-20 --days_ahead 10

5. **Open with Web UI:**

   ```bash
   python app.py

## Special Thanks

My liver. Literally spent 5 hours on sleeping and the rest all on this project. I would feel guilty if I have a teammate :)


![GitHub last commit](https://img.shields.io/github/last-commit/weizhi-du/duxchange)
![GitHub license](https://img.shields.io/github/license/weizhi-du/duxchange)
