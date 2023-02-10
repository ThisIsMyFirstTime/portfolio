from api.api_connection import WeatherAPI, ForecastAPI


if __name__ == "__main__":
    API_KEY = 'c077415b0bf4406b9fd223106230702'
    location = '76017'
    weather = WeatherAPI(API_KEY, location)
    forecast = ForecastAPI(API_KEY, location, 2)
    print(weather.to_dict['current'])
    print(weather.current_temp)
    for i in forecast.to_dict['forecast']['forecastday']:
        print(i['day'])

