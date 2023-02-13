import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

from api.api_connection import WeatherAPI, ForecastAPI


day_dict = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
            }


def _day_of_week():
    return datetime.today().isoweekday()


def next_6_days() -> list:
    day_int = _day_of_week()
    days_left = 7 - day_int
    next_6 = []
    for i in range(day_int, day_int + days_left + 1):
        next_6.append(day_dict[i])
    for i in range(1, day_int):
        next_6.append(day_dict[i])

    return next_6


API_KEY = 'c077415b0bf4406b9fd223106230702'
ZIP_CODE = '76017'

# initializing API classes
weather = WeatherAPI(API_KEY, ZIP_CODE)
forecast = ForecastAPI(API_KEY, ZIP_CODE, 7)


def main_loop():
    # Root window
    root = tk.Tk()
    root.geometry("900x300")
    root.title('Weather App')
    root.option_add('*tearOFF', False)
    root.maxsize(900, 300)

    # All icon images from API
    with Image.open(weather.raw_image) as image1:
        test = ImageTk.PhotoImage(image1)

    with Image.open(forecast.raw_image_day(2)) as image2:
        test2 = ImageTk.PhotoImage(image2)

    with Image.open(forecast.raw_image_day(3)) as image3:
        test3 = ImageTk.PhotoImage(image3)

    with Image.open(forecast.raw_image_day(4)) as image4:
        test4 = ImageTk.PhotoImage(image4)

    with Image.open(forecast.raw_image_day(5)) as image5:
        test5 = ImageTk.PhotoImage(image5)

    with Image.open(forecast.raw_image_day(6)) as image6:
        test6 = ImageTk.PhotoImage(image6)

    with Image.open(forecast.raw_image_day(7)) as image7:
        test7 = ImageTk.PhotoImage(image7)

    # main Frame init
    main = ttk.Frame(root, height='850', width='300')

    # main contents
    weather_frame = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)
    weather_frame2 = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)
    weather_frame3 = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)
    weather_frame4 = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)
    weather_frame5 = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)
    weather_frame6 = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)
    weather_frame7 = ttk.Frame(main, style='weather_frame.TFrame', height=400, width=85)


    # weather_frame1 contents
    label_day = ttk.Label(weather_frame, text=next_6_days()[0])
    label = ttk.Label(weather_frame, text=str(weather.temp))
    icon_label = ttk.Label(weather_frame, image=test)

    # weather_frame2 contents
    label_day2 = ttk.Label(weather_frame2, text=next_6_days()[1])
    label2 = ttk.Label(weather_frame2, text=str(forecast.temp_day(2)))
    icon_label2 = ttk.Label(weather_frame2, image=test2)

    # weather_frame3 contents
    label_day3 = ttk.Label(weather_frame3, text=next_6_days()[2])
    label3 = ttk.Label(weather_frame3, text=str(forecast.temp_day(3)))
    icon_label3 = ttk.Label(weather_frame3, image=test3)

    # weather_frame4 contents
    label_day4 = ttk.Label(weather_frame4, text=next_6_days()[3])
    label4 = ttk.Label(weather_frame4, text=str(forecast.temp_day(4)))
    icon_label4 = ttk.Label(weather_frame4, image=test4)

    # weather_frame5 contents
    label_day5 = ttk.Label(weather_frame5, text=next_6_days()[4])
    label5 = ttk.Label(weather_frame5, text=str(forecast.temp_day(5)))
    icon_label5 = ttk.Label(weather_frame5, image=test5)

    # weather_frame6 contents
    label_day6 = ttk.Label(weather_frame6, text=next_6_days()[5])
    label6 = ttk.Label(weather_frame6, text=str(forecast.temp_day(6)))
    icon_label6 = ttk.Label(weather_frame6, image=test6)

    # weather_frame7 contents
    label_day7 = ttk.Label(weather_frame7, text=next_6_days()[6])
    label7 = ttk.Label(weather_frame7, text=str(forecast.temp_day(7)))
    icon_label7 = ttk.Label(weather_frame7, image=test7)

    # Frame 1 packing
    label_day.pack(side='top')
    icon_label.pack(side='top')
    label.pack(side='top')

    # Frame 2 packing
    label_day2.pack(side='top')
    icon_label2.pack(side='top')
    label2.pack(side='top')

    # Frame 3 packing
    label_day3.pack(side='top')
    icon_label3.pack(side='top')
    label3.pack(side='top')

    # Frame 4 packing
    label_day4.pack(side='top')
    icon_label4.pack(side='top')
    label4.pack(side='top')

    # Frame 5 packing
    label_day5.pack(side='top')
    icon_label5.pack(side='top')
    label5.pack(side='top')

    # Frame 6 packing
    label_day6.pack(side='top')
    icon_label6.pack(side='top')
    label6.pack(side='top')

    # Frame 7 packing
    label_day7.pack(side='top')
    icon_label7.pack(side='top')
    label7.pack(side='top')

    # weather_frame packing
    weather_frame.pack(side='left', padx=10)
    weather_frame2.pack(side='left', padx=10)
    weather_frame3.pack(side='left', padx=10)
    weather_frame4.pack(side='left', padx=10)
    weather_frame5.pack(side='left', padx=10)
    weather_frame6.pack(side='left', padx=10)
    weather_frame7.pack(side='left', padx=10)

    main.pack(side='bottom', pady=90)

    root.mainloop()