import requests

from datetime import datetime

api_key = 'ed4db8b71a867fa02ab0c198a2c7fa9c'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")


with open('demo.txt', 'w+') as fh:
    fh.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))

    fh.write("temp_city :%f\nweather_desc :%s\nwind_spd :%f\nhumidity :%f "%(temp_city,weather_desc,wind_spd,humidity) )


