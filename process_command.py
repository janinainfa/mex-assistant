import configparser
import re
import subprocess
import custom_commands as cc
from voice_operations import *

class CommandProcessing():
    def __init__(self):
        pass

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.config = config

    def processCommand(self, window):
        command = takeVoice(3, window)
        window.stateLabel.setText(command)
        window.repaint()
        command = command.lower()
        self.loadConfig()
        for i in self.config:
            if re.search(i, command):
                try:
                    if self.config[i]["type"] == "terminal":
                        subprocess.Popen(self.config[i]["command"].split(" "))
                    elif self.config[i]["type"] == "python":
                        exec(self.config[i]["command"])
                    else:
                        speak("Nie udało się rozpoznać typu polecenia")
                except:
                    speak("Coś poszło nie tak. Upewnij się, że polecenie jest ustawione poprawnie")

                break


