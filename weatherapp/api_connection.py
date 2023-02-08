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
    def current_temp(self):
        return self.to_dict['current']['temp_f']

    @property
    def current_condition(self):
        return self.to_dict['current']['condition']['text']

    @property
    def current_condition_icon(self):
        return self.to_dict['current']['condition']['icon']

    def image_grab(self):
        url = "https:" + self.current_condition_icon
        response = requests.get(url)
        if response.status_code == 200:
            with open('weather.json', 'wb') as f:
                f.write(response.content)


class NotScriptError(Exception):
    pass


if __name__ == '__main__':
    raise NotScriptError('This is not a script.')
