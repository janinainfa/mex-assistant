import subprocess

import requests
import translators as ts
import os
import urllib.request
import re

from pytube import YouTube


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

def downloadFromYT(query):
    yt = YouTube(searchOnYT(query))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download("~/Muzyka")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(new_file)
    subprocess.Popen(['rhythmbox', new_file])

def searchOnYT(query):
    search_keyword = query.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]