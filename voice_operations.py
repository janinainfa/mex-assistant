import sounddevice as sd
import speech_recognition as sr
import soundfile as sf

from gtts import gTTS

from pydub import AudioSegment
from pydub.playback import play

def speak(text):
    myobj = gTTS(text=text, lang='pl', slow=False)
    myobj.save("output.mp3")
    sound = AudioSegment.from_mp3('output.mp3')
    play(sound)

def takeVoice(time):
    r = sr.Recognizer()
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