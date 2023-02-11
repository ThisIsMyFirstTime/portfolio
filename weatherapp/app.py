from api.api_connection import WeatherAPI, ForecastAPI
from datetime import datetime

if __name__ == "__main__":
    API_KEY = 'c077415b0bf4406b9fd223106230702'
    location = '76017'
    weather = WeatherAPI(API_KEY, location)
    forecast = ForecastAPI(API_KEY, location, 3)
    print(datetime.today().isoweekday())

