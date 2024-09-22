// src/components/PredictionPlots.js

import React from 'react';

function PredictionPlots({ ticker }) {
  const predictionPlotURL = `http://localhost:5000/api/plots/${ticker}/prediction`; // Update to point to Flask API
  const futurePredictionPlotURL = `http://localhost:5000/api/plots/${ticker}/future_prediction`; // Update to Flask API

  return (
    <div>
      <h2>{ticker} Prediction Plot</h2>
      <img src={predictionPlotURL} alt="Prediction Plot" width="800" />
      <h2>{ticker} Future Prediction Plot</h2>
      <img src={futurePredictionPlotURL} alt="Future Prediction Plot" width="800" />
    </div>
  );
}

export default PredictionPlots;
