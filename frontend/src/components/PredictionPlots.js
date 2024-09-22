// src/components/PredictionPlots.js

import React from 'react';

function PredictionPlots({ ticker }) {
  const predictionPlotURL = `/api/plots/${ticker}/prediction`;
  const futurePredictionPlotURL = `/api/plots/${ticker}/future_prediction`;

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
