import requests
import json



class WeatherAPI:
    def __init__(self, api_key, location):
        self.url = 'https://api.weatherapi.com/v1/current.json?key=' + str(api_key) + "&q=" + str(location)

    @property
    def response(self):
        return requests.get(self.url)

    @property
    def to_dict(self):
        return self.response.json()

    @property
    def temp(self):
        return self.to_dict['current']['temp_f']

    @property
    def condition(self):
        return self.to_dict['current']['condition']['text']

    @property
    def icon_url(self):
        return self.to_dict['current']['condition']['icon']

    @property
    def raw_image(self):
        url = 'https:' + self.icon_url
        return requests.get(url, stream=True).raw


class ForecastAPI(WeatherAPI):
    def __init__(self, api_key, location, days=None, hour=None):
        super().__init__(api_key, location)
        self.url = 'https://api.weatherapi.com/v1/forecast.json?key='
        self.url += str(api_key) + '&q=' + str(location) + '&days=' + str(days) + '&hour=' + str(hour)

    @property
    def temp(self):
        return self.to_dict['forecast']['forecastday'][1]['hour']

    @property
    def condition(self):
        return self.to_dict['forecast']['condition']['forecastday']['day']['text']

    @property
    def icon_url(self):
        return self.to_dict['forecast']['condition']['forecastday']['day']['icon']

    @property
    def raw_image(self):
        url = 'https:' + self.icon_url
        return requests.get(url, stream=True).raw


class NotScriptError(Exception):
    pass


if __name__ == '__main__':
    raise NotScriptError("This is not a script.")
