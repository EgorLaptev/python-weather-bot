import requests
from config import GEOCODER_TOKEN


class Geocoder:
    
    _api = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode=%s'

    @staticmethod
    def get(city):
        try:
            resp = requests.get(Geocoder._api % (GEOCODER_TOKEN, city))
            data = resp.json()['response']['GeoObjectCollection']['featureMember']

            lon, lat = data[0]['GeoObject']['Point']['pos'].split()
            return [lon, lat]
            
        except Exception as error:
            return 'unknown city'

