import requests


class WeatherAPI:
    def __init__(self, api_key, location):
        self.url = 'https://api.weatherapi.com/v1/current.json?key=' + str(api_key) + "&q=" + str(location)

    def response(self):
        return requests.get(self.url)

    def to_dict(self):
        return self.response().json()






if __name__ == '__main__':
    weather = WeatherAPI()
    print(weather.response)