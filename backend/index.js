// backend/index.js
const express = require('express');
const cors = require('cors');
const axios = require('axios');
require('dotenv').config();

const app = express();
app.use(cors());

const PORT = process.env.PORT || 5001;
const API_KEY = process.env.ODDS_API_KEY;

app.get('/api/arbitrage', async (req, res) => {
  try {
    const response = await axios.get('https://api.the-odds-api.com/v4/sports/upcoming/odds', {
      params: {
        apiKey: API_KEY,
        regions: 'us',
        markets: 'h2h',
        oddsFormat: 'american'
      }
    });

    const games = response.data;
    const arbitrageOpportunities = [];

    for (const game of games) {
      const outcomes = {};

      for (const bookmaker of game.bookmakers) {
        for (const market of bookmaker.markets) {
          for (const outcome of market.outcomes) {
            const name = outcome.name;
            const odds = outcome.price;

            if (!outcomes[name] || odds > outcomes[name].odds) {
              outcomes[name] = { odds, bookmaker: bookmaker.title };
            }
          }
        }
      }

      const impliedTotal = Object.values(outcomes).reduce((acc, curr) => {
        const odds = curr.odds;
        return acc + (odds > 0 ? 100 / (odds + 100) : Math.abs(odds) / (Math.abs(odds) + 100));
      }, 0);

      if (impliedTotal < 1) {
        arbitrageOpportunities.push({
          sport: game.sport_title,
          teams: game.home_team + ' vs ' + game.away_team,
          outcomes,
          impliedTotal: impliedTotal.toFixed(3),
          profitMargin: ((1 - impliedTotal) * 100).toFixed(2) + '%'
        });
      }
    }

    res.json(arbitrageOpportunities);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to fetch odds' });
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
