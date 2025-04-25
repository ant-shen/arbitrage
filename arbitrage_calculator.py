import numpy as np
from typing import List, Tuple, Dict

class ArbitrageCalculator:
    def __init__(self):
        self.bookmakers = {}
    
    def add_bookmaker(self, name: str, odds: Dict[str, float]):
        """
        Add a bookmaker's odds to the calculator
        """
        self.bookmakers[name] = odds
    
    def calculate_arbitrage(self) -> List[Dict]:
        """
        Calculate arbitrage opportunities across all bookmakers
        Returns a list of arbitrage opportunities
        """
        opportunities = []
        
        # Get all unique outcomes
        all_outcomes = set()
        for odds in self.bookmakers.values():
            all_outcomes.update(odds.keys())
        
        # Check each outcome combination
        for outcome in all_outcomes:
            best_odds = {}
            for bookie, odds_dict in self.bookmakers.items():
                if outcome in odds_dict:
                    if outcome not in best_odds or odds_dict[outcome] > best_odds[outcome][1]:
                        best_odds[outcome] = (bookie, odds_dict[outcome])
            
            if len(best_odds) >= 2:  # Need at least 2 bookmakers for arbitrage
                total_probability = sum(1/odds for _, odds in best_odds.values())
                
                if total_probability < 1:  # Arbitrage opportunity exists
                    profit_percentage = (1 - total_probability) * 100
                    opportunity = {
                        'outcome': outcome,
                        'best_odds': best_odds,
                        'profit_percentage': profit_percentage,
                        'recommended_bets': self._calculate_optimal_bets(best_odds)
                    }
                    opportunities.append(opportunity)
        
        return opportunities
    
    def _calculate_optimal_bets(self, best_odds: Dict[str, Tuple[str, float]], 
                              total_investment: float = 1000) -> Dict[str, Dict]:
        """
        Calculate the optimal bet amounts for each outcome
        """
        total_probability = sum(1/odds for _, odds in best_odds.values())
        optimal_bets = {}
        
        for outcome, (bookie, odds) in best_odds.items():
            bet_amount = (total_investment / odds) / total_probability
            optimal_bets[outcome] = {
                'bookmaker': bookie,
                'odds': odds,
                'amount': round(bet_amount, 2),
                'potential_return': round(bet_amount * odds, 2)
            }
        
        return optimal_bets
    
    def get_bookmaker_odds(self, bookmaker: str) -> Dict[str, float]:
        """
        Get odds for a specific bookmaker
        """
        return self.bookmakers.get(bookmaker, {})
    
    def get_all_bookmakers(self) -> List[str]:
        """
        Get list of all bookmakers
        """
        return list(self.bookmakers.keys()) 