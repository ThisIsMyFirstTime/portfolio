import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

from api.api_connection import WeatherAPI, ForecastAPI


API_KEY = 'c077415b0bf4406b9fd223106230702'
ZIP_CODE = '76017'

weather = WeatherAPI(API_KEY, ZIP_CODE)
forecast = ForecastAPI(API_KEY, ZIP_CODE, 2)

root = tk.Tk()
root.geometry("900x300")
root.title('Weather App')
root.option_add('*tearOFF', False)
root.maxsize(900, 300)

style = ttk.Style()
style.configure('')

with Image.open(weather.raw_image) as image1:
    test = ImageTk.PhotoImage(image1)

with Image.open(forecast.raw_image) as image1:
    test2 = ImageTk.PhotoImage(image1)

main = ttk.Frame(root, height='850', width='200')
weather_frame = ttk.Frame(main, height=85, width=85)
weather_frame2 = ttk.Frame(main, height=85, width=85)

label = ttk.Label(weather_frame, text=str(weather.temp))
icon_label = ttk.Label(weather_frame, image=test)

label2 = ttk.Label(weather_frame2, text=str(forecast.temp))
icon_label2 = ttk.Label(weather_frame2, image=test2)

icon_label.pack(side='top')
label.pack(side='top')

icon_label2.pack(side='top')
label2.pack(side='top')

weather_frame.pack(side='left')
weather_frame2.pack(side='left')

main.pack(side='bottom', pady=100)

root.mainloop()