import requests




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

        self.weather = self.to_dict['forecast']['forecastday']

    def temp_day(self, day: int):
        return self.weather[day - 1]['day']['avgtemp_f']

    def condition_day(self, day: int):
        return self.weather[day - 1]['day']['condition']['text']

    def icon_url_day(self, day: int) -> str:
        return self.weather[day - 1]['day']['condition']['icon']

    def raw_image_day(self, day):
        url = 'https:' + self.icon_url_day(day)
        return requests.get(url, stream=True).raw


class NotScriptError(Exception):
    pass


if __name__ == '__main__':
    raise NotScriptError("This is not a script.")
