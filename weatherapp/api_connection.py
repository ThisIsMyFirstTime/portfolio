import requests


class WeatherAPI:
    API_KEY = 'c077415b0bf4406b9fd223106230702'

    base_url = 'https://api.weatherapi.com/v1/c077415b0bf4406b9fd223106230702/current.json'

    def __init__(self):
        self.response = requests.get(self.base_url)


if __name__ == '__main__':
    weather = WeatherAPI()
    print(weather.response)