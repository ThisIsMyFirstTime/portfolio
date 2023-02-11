import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

from api.api_connection import WeatherAPI


API_KEY = 'c077415b0bf4406b9fd223106230702'
ZIP_CODE = '76017'

weather = WeatherAPI(API_KEY, ZIP_CODE)

root = tk.Tk()
root.geometry("650x250")
root.title('Weather App')
root.option_add('*tearOFF', False)



with Image.open(weather.raw_image) as image1:
    test = ImageTk.PhotoImage(image1)

main = ttk.Frame(root, height='1200', width='900')
weather_frame = ttk.Frame(main)

weather_label_frame1 = ttk.LabelFrame(weather_frame)
weather_label_frame2 = ttk.LabelFrame(weather_frame)
weather_label_frame3 = ttk.LabelFrame(weather_frame)
weather_label_frame4 = ttk.LabelFrame(weather_frame)
weather_label_frame5 = ttk.LabelFrame(weather_frame)
weather_label_frame6 = ttk.LabelFrame(weather_frame)
weather_label_frame7 = ttk.LabelFrame(weather_frame)

condition1 = ttk.Label(weather_label_frame1, image=test)
label1 = ttk.Label(weather_label_frame1, text=str(weather.temp))

condition2 = ttk.Label(weather_label_frame1, image=test)
label2 = ttk.Label(weather_label_frame1, text=str(weather.temp))

condition3 = ttk.Label(weather_label_frame1, image=test)
label3 = ttk.Label(weather_label_frame1, text=str(weather.temp))

condition4 = ttk.Label(weather_label_frame1, image=test)
label4 = ttk.Label(weather_label_frame1, text=str(weather.temp))

condition5 = ttk.Label(weather_label_frame1, image=test)
label5 = ttk.Label(weather_label_frame1, text=str(weather.temp))

condition6 = ttk.Label(weather_label_frame1, image=test)
label6 = ttk.Label(weather_label_frame1, text=str(weather.temp))

condition7 = ttk.Label(weather_label_frame1, image=test)
label7 = ttk.Label(weather_label_frame1, text=str(weather.temp))

main.pack()

condition1.pack(side='top')
label1.pack(side='top')

condition2.pack(side='top')
label2.pack(side='top')

condition3.pack(side='top')
label3.pack(side='top')

condition4.pack(side='top')
label4.pack(side='top')

condition5.pack(side='top')
label5.pack(side='top')

condition6.pack(side='top')
label6.pack(side='top')

condition7.pack(side='top')
label7.pack(side='top')

weather_label_frame1.pack(side='left')
weather_label_frame2.pack(side='left')
weather_label_frame3.pack(side='left')
weather_label_frame4.pack(side='left')
weather_label_frame5.pack(side='left')
weather_label_frame6.pack(side='left')
weather_label_frame7.pack(side='left')



root.mainloop()