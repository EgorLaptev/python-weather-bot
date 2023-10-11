import requests


class Geocoder:
    _token = 'e8d11b29-ac13-4d58-9091-bc3c84473d2d'
    _api = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode=%s'

    @staticmethod
    def get(city):
        resp = requests.get(Geocoder._api % (Geocoder._token, city))
        data = resp.json()['response']['GeoObjectCollection']['featureMember']

        if len(data):
            lon, lat = data[0]['GeoObject']['Point']['pos'].split()
            return [lon, lat]
        else:
            raise Exception('unknown')

