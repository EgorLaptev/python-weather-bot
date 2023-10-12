import requests
from config import WEATHER_TOKEN
from models.Geocoder import Geocoder


class Weather:

    _api = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&lang=%s'

    @staticmethod
    def get(city):

        try: 
            lon, lat = Geocoder.get(city)

            url = Weather._api % (lat, lon, 'ru_RU')
            headers = {'X-Yandex-API-Key': WEATHER_TOKEN}

            resp = requests.get(url, headers=headers)
            data = resp.json()

            return data
        except Exception as error:
            return 'unknown city'

