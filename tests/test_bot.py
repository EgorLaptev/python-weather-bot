import unittest
from models.Weather import Weather
from models.Geocoder import Geocoder

class CalculatorTestCase(unittest.TestCase):
    
    def test_english(self):
        self.assertEqual(Weather.get('Moscow')['info']['tzinfo']['name'], 'Europe/Moscow')
        
    def test_russian(self):
        self.assertEqual(Weather.get('Санкт-Петербург')['info']['tzinfo']['name'], 'Europe/Moscow')
        
    def test_abroad(self):
        self.assertEqual(Weather.get('Mayami')['info']['tzinfo']['name'], 'America/New_York')
        
    def test_not_existing(self):
        self.assertEqual(Weather.get('this city does not existing'), 'unknown city')

    def test_bullshit(self):
        self.assertEqual(Weather.get('#$g4'), 'unknown city')

    def test_correct(self):
        self.assertEqual(Geocoder.get('Moscow'), ['37.617698', '55.755864'])

    def test_correct(self):
        self.assertEqual(Geocoder.get('Якутия'), ['119.845661', '65.061073'])

    def test_invalid(self):
        self.assertEqual(Geocoder.get('bullshit'), 'unknown city')

        