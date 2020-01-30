import os

class GameStats:
    """Tracks statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in active state.
        self.game_active = False
        
        try:
            with open('high_score.txt','rt') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            with open('high_score.txt','wt') as f:
                f.write("0")
                self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1