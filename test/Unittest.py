import json
from pathlib import Path
import unittest

# Functie om de score op te halen
def get_high_score():
    """Highscore ophalen uit bestand als het bestand bestaat, anders 0 geven"""
    path = Path('at_high_score.json')
    if path.exists():
        contents = path.read_text()
        return int(json.loads(contents))
    return 0


# Functie om score op te slaan
def quit_game(stats):
    """Nieuwe highscore opslaan als deze hoger is dan de huidig highscore"""
    at_high_score = get_high_score()
    if stats > at_high_score:
        path = Path('at_high_score.json')
        contents = json.dumps(stats)
        path.write_text(contents)
        

# Testclass om de highscore ophaal/opslaan functies te testen.
class TestHighscore(unittest.TestCase):
    
    def setUp(self):
       """Haalt het bestand weg voor de 'geen bestand'-test"""
       path = Path('at_high_score.json')
       if path.exists():
           path.unlink() 

    def test_get_high_score_geen_bestand(self):
        """Checkt of er 0 geretourneerd wordt als er geen bestand is."""
        self.assertEqual(get_high_score(), 0)

    def test_get_high_score(self):
        """Test of de waarde van de highscore wordt opgehaald"""
        quit_game(200)
        self.assertEqual(get_high_score(), 200)

    def test_new_high_score(self):
        """Checkt of de nieuwe highscore de oude overschrijft"""
        quit_game(100)
        quit_game(200)
        self.assertEqual(get_high_score(), 200)

    def test_no_new_high_score(self):
        """Checkst of een lagere score niet de highscore overschrijft"""
        quit_game(200)
        quit_game(100)
        self.assertEqual(get_high_score(), 200)

unittest.main()