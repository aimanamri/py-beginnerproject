import requests
from datetime import datetime
from tkinter import *
from tkinter import messagebox
# import os  # API key stored in .env file
from dotenv import load_dotenv
import os

load_dotenv()
API_key = os.getenv('API_KEY')

def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_key
    api_data = requests.get(url).json()
    #(City, Country,temp_celcius,temp_fahrenheit,icon,weather)

    if api_data['cod'] == '404':
        return
    else:
        city = api_data['name']
        country = api_data['sys']['country']
        temp_celcius = ((api_data['main']['temp'])-273.15) #JSON data temp in Kelvin unit
        temp_fahrenheit = (((api_data['main']['temp'])-273.15)*(9/5)+32)
        icon = api_data['weather'][0]['icon']
        weather = api_data['weather'][0]['main']
        weather_desc = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p"  )
        final = (city,country,temp_celcius,temp_fahrenheit,icon,weather)
        return final

def search(): 
    global img
    city = city_text.get()
    weather = get_weather(city)
    img["file"] = 'weather_icons\\{}.png'.format(weather[4])
    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        temp_lbl['text'] = f'{weather[2]:.2f}°C, {weather[3]:.2f}°F'
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('Error',f'Cannot find city {city}')

app = Tk()
app.title("Weather App")
app.geometry('250x300')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app,text="Search weather",width=12,command=search)
search_btn.pack()

location_lbl = Label(app,text='', font=('bold',20))
location_lbl.pack()

img = PhotoImage(file="")
Image = Label(app, image=img)
Image.pack()

temp_lbl = Label(app,text="")
temp_lbl.pack()

weather_lbl = Label(app,text="")
weather_lbl.pack()

app.mainloop()
