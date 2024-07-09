import os

homeDir = os.path.expanduser("~")


configContent = '''[DEFAULT]
voice_lang = pl-PL

[otwórz terminal]
type = terminal
command = gnome-terminal

[zakończ]
type = python
command = window.close()

[pogoda]
type = python
command = results = gw.getWeather()
	speak(f"Jest {results[0]} stopni, odczuwalne {results[1]} stopni i {results[2]}")
	
[puść muzykę]
type = terminal
command = playerctl play

[zatrzymaj muzykę]
type = terminal
command = playerctl pause

[następna piosenka]
type = terminal
command = playerctl next'''

def createConfig():
    try:
        os.mkdir(homeDir + "/mexassistant")
    except:
        pass
    finally:
        with open(homeDir + "/mexassistant/config.ini", 'w') as f:
            f.write(configContent)


