from api_connection import WeatherAPI


if __name__ == "__main__":
    API_KEY = 'c077415b0bf4406b9fd223106230702'
    location = '76017'
    weather = WeatherAPI(API_KEY, location)
    print(weather.to_dict['current']['condition'])
    weather.current_condition_icon
    weather.image_grab()


