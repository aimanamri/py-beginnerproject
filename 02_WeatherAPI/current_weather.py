import requests
from datetime import datetime
# import os  #store API key in system env 

API_key = '<------>' #put API key here

location = input("Enter the city name :  ")
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + str(API_key)

api_data = requests.get(url).json()

if api_data['cod'] == '404':
    print(f'Invalid City : {location} | Please check your city name')
else:
    city = api_data['name']
    country = api_data['sys']['country']
    temp_city_C = ((api_data['main']['temp'])-273.15) 
    temp_city_K = (((api_data['main']['temp'])-273.15)*(9/5)+32)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p"  )

    print("------------------------------------------------------------")
    print(f'Weather Stats for - {city}, {country} || {date_time}')
    print("------------------------------------------------------------")

    print(f'Current temperature : {temp_city_C:.2f} °C, {temp_city_K:.2f} °F')
    print(f'Current weather : {weather_desc}')
    print(f'Current humidity : {humidity} % ')
    print(f'Current wind speed : {wind_spd} m/s')

print("------------------------------------------------------------")
print("------------------------------------------------------------")