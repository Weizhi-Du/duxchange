// src/components/PredictionChart.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend } from 'recharts';

function PredictionChart({ ticker }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`/api/predictions/${ticker}`)
      .then(response => {
        if (response.data.predictions) {
          setData(response.data.predictions);
        } else {
          alert('No prediction data found.');
        }
      })
      .catch(error => {
        console.error('Error fetching prediction data:', error);
      });
  }, [ticker]);

  return (
    <div>
      <h2>{ticker} Future Predictions</h2>
      <LineChart width={800} height={400} data={data}>
        <XAxis dataKey="Date" />
        <YAxis domain={['auto', 'auto']} />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="Predicted_Price" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default PredictionChart;
