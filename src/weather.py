import tkinter as tk
import requests
import time


def getWeather(canvas):
    location = textfield.get()

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=763e10b82c000e0f3f45b397481022f3"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int((((json_data['main']['temp'] - 273.15) * 9) / 5) + 32)
    min_temp = int((((json_data['main']['temp_min'] - 273.15) * 9) / 5) + 32)
    max_temp = int((((json_data['main']['temp_max'] - 273.15) * 9) / 5) + 32)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 18000))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 18000))

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " \
                 + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + \
                 "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(bg="white", text=final_info )
    label2.config(bg="white", text=final_data )


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.config(bg="white")

f = ("open sans", 16, "bold")
t = ("open sans", 35, "bold")

textfield = tk.Entry(canvas, font=f)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.config(bg="white")
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.config(bg="white")
label2.pack()

canvas.mainloop()
