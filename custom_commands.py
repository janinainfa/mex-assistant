import requests
import translators as ts

def getWeather():
    api_key = "fa46bb6b7badd2d6a93fa08a2da9b45e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=Poznań"
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = int(round(y["temp"] - 272.15))
    current_feel = int(round(y["feels_like"] - 272.15))
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = ts.translate_text(z[0]["description"], to_language='pl')
    return [current_temperature, current_feel, weather_description]