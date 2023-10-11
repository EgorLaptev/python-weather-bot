import requests
from models.Geocoder import Geocoder


class Weather:

    _token = 'b320f71a-cb78-44d1-b4c9-d25b5137f8df'
    _api = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&lang=%s'

    @staticmethod
    def get(city):

        lon, lat = Geocoder.get(city)

        url = Weather._api % (lat, lon, 'ru_RU')
        headers = {'X-Yandex-API-Key': Weather._token}

        resp = requests.get(url, headers=headers)
        data = resp.json()['fact']

        return data


