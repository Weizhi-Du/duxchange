// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


// src/App.js

import React, { useState } from 'react';
import PredictionChart from './components/PredictionChart';
import PredictionPlots from './components/PredictionPlots';

function App() {
  const [ticker, setTicker] = useState('AAPL');
  const [submittedTicker, setSubmittedTicker] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmittedTicker(ticker.toUpperCase());
  };

  return (
    <div className="App">
      <h1>Stock Prediction Viewer</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter Stock Ticker Symbol:
          <input
            type="text"
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
            required
          />
        </label>
        <button type="submit">View Predictions</button>
      </form>

      {submittedTicker && (
        <div>
          <PredictionPlots ticker={submittedTicker} />
          <PredictionChart ticker={submittedTicker} />
        </div>
      )}
    </div>
  );
}

export default App;
