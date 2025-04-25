import random
from typing import Dict, List
import time

class OddsFetcher:
    def __init__(self):
        self.bookmakers = {
            'Bet365': 'https://api.bet365.com',
            'WilliamHill': 'https://api.williamhill.com',
            'Betway': 'https://api.betway.com',
            'Unibet': 'https://api.unibet.com'
        }
    
    def fetch_odds(self, sport: str, event: str) -> Dict[str, Dict[str, float]]:
        """
        Fetch odds from all bookmakers for a specific sport and event
        This is a mock implementation - replace with real API calls
        """
        all_odds = {}
        
        for bookie in self.bookmakers:
            # Simulate API call delay
            time.sleep(0.1)
            
            # Generate mock odds with some randomness
            if sport.lower() == 'football':
                odds = self._generate_football_odds()
            elif sport.lower() == 'basketball':
                odds = self._generate_basketball_odds()
            else:
                odds = self._generate_generic_odds()
            
            all_odds[bookie] = odds
        
        return all_odds
    
    def _generate_football_odds(self) -> Dict[str, float]:
        """
        Generate mock football odds
        """
        home_win = round(random.uniform(1.5, 3.5), 2)
        draw = round(random.uniform(2.8, 4.2), 2)
        away_win = round(random.uniform(1.5, 3.5), 2)
        
        return {
            'Home Win': home_win,
            'Draw': draw,
            'Away Win': away_win
        }
    
    def _generate_basketball_odds(self) -> Dict[str, float]:
        """
        Generate mock basketball odds
        """
        home_win = round(random.uniform(1.3, 2.5), 2)
        away_win = round(random.uniform(1.3, 2.5), 2)
        
        return {
            'Home Win': home_win,
            'Away Win': away_win
        }
    
    def _generate_generic_odds(self) -> Dict[str, float]:
        """
        Generate mock generic odds
        """
        return {
            'Outcome 1': round(random.uniform(1.5, 3.0), 2),
            'Outcome 2': round(random.uniform(1.5, 3.0), 2)
        }
    
    def get_available_sports(self) -> List[str]:
        """
        Get list of available sports
        """
        return ['Football', 'Basketball', 'Tennis', 'Baseball']
    
    def get_available_events(self, sport: str) -> List[str]:
        """
        Get list of available events for a sport
        """
        if sport.lower() == 'football':
            return ['Manchester United vs Liverpool', 'Barcelona vs Real Madrid', 
                   'Bayern Munich vs Dortmund']
        elif sport.lower() == 'basketball':
            return ['Lakers vs Warriors', 'Celtics vs Nets', 'Bucks vs Heat']
        else:
            return ['Event 1', 'Event 2', 'Event 3'] 