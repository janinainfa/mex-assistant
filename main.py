import os
import subprocess
import sounddevice as sd
import speech_recognition as sr
import soundfile as sf
from tkinter import *
from gtts import gTTS
import webbrowser
import requests
import translators as ts
from pytube import YouTube
import urllib.request
import re
import datetime
import json
from pydub import AudioSegment
from pydub.playback import play

tk = Tk()
tk.title("Mex Assistant")
tk.wm_attributes("-topmost", True)
r = sr.Recognizer()

def speak(text):
    myobj = gTTS(text=text, lang='pl', slow=False)
    myobj.save("output.mp3")
    sound = AudioSegment.from_mp3('output.mp3')
    play(sound)

def takeVoice(time):
    speak('Mów')
    print("Nagrywanie")
    myrecording = sd.rec(int(time * 44100), samplerate=44100, channels=2)
    sd.wait()  # Wait until recording is finished
    sf.write('input.flac', myrecording, 44100)  # Save as WAV file
    print("Rozpoznawanie")

    file = sr.AudioFile('input.flac')

    with file as source:
        audio = r.record(source)

    return r.recognize_google(audio, language="pl-PL")

def downloadFromYT(query):
    yt = YouTube(searchOnYT(query))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download("/home/jacek/Muzyka")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(new_file)
    os.system(f'rhythmbox "{new_file}"')

def searchOnYT(query):
    search_keyword = query.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]

def pogoda():
    # Google Open weather website
    # to get API of Open weather
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
    speak(f"Jest {current_temperature} stopni, odczuwalne {current_feel} stopni i {weather_description}")

def onClick():
    command = takeVoice(3)
    command = command.lower()
    print(command)
    if 'godzina' in command:
        time = datetime.datetime.now()
        strTime = time.strftime("%H:%M:%S")
        speak(f'Jest godzina {strTime}')

    elif 'zakończ' in command:
        speak("Zamykanie")
        tk.destroy()

    elif "szukaj" in command:
        query = command.replace("szukaj", "")
        speak(f"Wyszukuję zapytania dla {query}")
        webbrowser.open(f"https://duckduckgo.com/?q={query}")

    elif "pogoda" in command:
        pogoda()

    elif "puść muzykę" in command:
        os.system("playerctl play")

    elif "zatrzymaj muzykę" in command:
        os.system("playerctl pause")

    elif "następna piosenka" in command:
        os.system("playerctl next")

    elif "pobierz muzykę" in command:
        speak("Podaj tytuł:")
        downloadFromYT(takeVoice(3))

    elif "włącz muzykę" in command:
        speak("Podaj tytuł:")
        webbrowser.open_new_tab(searchOnYT(takeVoice(3)))

    elif "otwórz" in command:
        if "spotify" in command: app = "spotify"
        elif "pliki" in command: app = "nemo"
        elif "monitor systemu" in command: app = "gnome-system-monitor"
        elif "terminal" in command: app = "gnome-terminal"
        elif "librus" in command: app = ["vivaldi", "synergia.librus.pl"]
        elif "bandlab" in command: app = ["vivaldi", "bandlab.com"]
        elif "jakdojade" in command: app = ["vivaldi", "jakdojade.pl"]
        else: return
        subprocess.Popen(app)

btn = Button(tk, text="Mów", command=onClick)
btn.pack()
speak("Dzień dobry")
tk.mainloop()
