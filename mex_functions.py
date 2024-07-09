import configparser

import sounddevice as sd
import speech_recognition as sr
import soundfile as sf
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from gtts import gTTS

from pydub import AudioSegment
from pydub.playback import play

def speak(text):
    myobj = gTTS(text=text, lang='pl', slow=False)
    myobj.save("output.mp3")
    sound = AudioSegment.from_mp3('output.mp3')
    play(sound)


def takeVoice(time, window=None):
    config = loadConfig()
    lang = config["DEFAULT"]["voice_lang"]
    r = sr.Recognizer()
    speak('Mów')
    printText("Nagrywanie", window)
    myrecording = sd.rec(int(time * 44100), samplerate=44100, channels=2)
    sd.wait()  # Wait until recording is finished
    sf.write('input.flac', myrecording, 44100)  # Save as WAV file
    printText("Rozpoznawanie", window)

    file = sr.AudioFile('input.flac')

    with file as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio, language=lang)
    except:
        speak("Nie udało się rozpoznać tekstu.")
        return ""

def printText(text, window):
    if window:
        window.stateLabel.setText(text)
        window.repaint()
    else:
        print(text)

def loadConfig():
    config = configparser.ConfigParser()
    config.read("/etc/mex-assistant/config.ini")
    return config

def openDialog(message, dialogType):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setText(message)
    if dialogType == 'confirmation':
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("Tak")
        msgBox.button(QMessageBox.No).setText("Nie")
    elif dialogType == "information":
        msgBox.setStandardButtons(QMessageBox.Ok)
    return msgBox.exec()