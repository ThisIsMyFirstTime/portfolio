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

style = ttk.Style()
style.configure('TFrame', background='blue')
style.configure('weather_frame1.TFrame', background='red', borderwidth=1)

weather_frame1 = ttk.Frame(root, style='weather_frame1.TFrame', height='100', width='100')


image1 = Image.open(weather.raw_image)
test = ImageTk.PhotoImage(image1)

label1 = ttk.Label(weather_frame1, image=test)
label1.pack(side='left', fill='both')
label2 = ttk.Label(weather_frame1, image=test)
label2.pack(side='left', fill='both')
label3 = ttk.Label(weather_frame1, image=test)
label3.pack(side='left', fill='both')
label4 = ttk.Label(weather_frame1, image=test)
label4.pack(side='left', fill='both')
label5 = ttk.Label(weather_frame1, image=test)
label5.pack(side='left', fill='both')
label6 = ttk.Label(weather_frame1, image=test)
label6.pack(side='left', fill='both')
label7 = ttk.Label(weather_frame1, image=test)
label7.pack(side='left', fill='both')

weather_frame1.pack()

root.mainloop()