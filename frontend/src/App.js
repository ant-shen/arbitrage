import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [arbs, setArbs] = useState([]);

  useEffect(() => {
    const fetchArbs = async () => {
      const res = await axios.get('http://localhost:5001/api/arbitrage');
      setArbs(res.data);
    };

    fetchArbs();
    const interval = setInterval(fetchArbs, 30000); // Refresh every 30s
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <h1>Sports Arbitrage Finder</h1>
      {arbs.length === 0 ? (
        <p>No opportunities found...</p>
      ) : (
        <div className="arb-list">
          {arbs.map((arb, i) => (
            <div key={i} className="arb-card">
              <h2>{arb.teams}</h2>
              <p><strong>Sport:</strong> {arb.sport}</p>
              <p><strong>Profit Margin:</strong> {arb.profitMargin}</p>
              {Object.entries(arb.outcomes).map(([team, data]) => (
                <p key={team}>
                  {team}: {data.odds} @ {data.bookmaker}
                </p>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
