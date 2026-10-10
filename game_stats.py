# -*- coding: utf-8 -*-
import json
from pathlib import Path


class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self.get_at_high_score()

    def get_at_high_score(self):
        """retrive highscore, if file doesn't exist highscore is 0"""
        path = Path('at_high_score.json')
        if path.exists():
            contents = path.read_text()
            return int(json.loads(contents))
        return 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
