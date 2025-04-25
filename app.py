from flask import Flask, render_template, request, jsonify
from arbitrage_calculator import ArbitrageCalculator
from odds_fetcher import OddsFetcher

app = Flask(__name__)
calculator = ArbitrageCalculator()
odds_fetcher = OddsFetcher()

@app.route('/')
def index():
    sports = odds_fetcher.get_available_sports()
    return render_template('index.html', sports=sports)

@app.route('/get_events/<sport>')
def get_events(sport):
    events = odds_fetcher.get_available_events(sport)
    return jsonify(events)

@app.route('/calculate', methods=['POST'])
def calculate():
    sport = request.form.get('sport')
    event = request.form.get('event')
    
    # Fetch odds from all bookmakers
    all_odds = odds_fetcher.fetch_odds(sport, event)
    
    # Add odds to calculator
    calculator.bookmakers = {}  # Reset calculator
    for bookie, odds in all_odds.items():
        calculator.add_bookmaker(bookie, odds)
    
    # Calculate arbitrage opportunities
    opportunities = calculator.calculate_arbitrage()
    
    return render_template('results.html', 
                         opportunities=opportunities,
                         sport=sport,
                         event=event,
                         all_odds=all_odds)

if __name__ == '__main__':
    app.run(debug=True) 