// src/components/PredictionChart.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';

function PredictionChart({ ticker }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/predictions/${ticker}`)
      .then(response => {
        if (response.data.predictions) {
          setData(response.data.predictions);  // Use setData to store predictions
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
      {data.length > 0 ? (
        <LineChart width={800} height={400} data={data}>
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <CartesianGrid stroke="#ccc" />
          <Line type="monotone" dataKey="Predicted_Price" stroke="#8884d8" />
        </LineChart>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default PredictionChart;
