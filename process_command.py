import re
import subprocess
import custom_commands as cc
from mex_functions import *

class CommandProcessing():

    def processCommand(self, window):
        command = takeVoice(3, window)
        window.stateLabel.setText(command)
        window.repaint()
        command = command.lower()
        config = loadConfig()
        for i in config.sections():
            if re.search(i, command):
                try:
                    if config[i]["type"] == "terminal":
                        subprocess.Popen(config[i]["command"].split(" "))
                    elif config[i]["type"] == "python":
                        exec(config[i]["command"])
                    else:
                        speak("Nie udało się rozpoznać typu polecenia")
                except:
                    speak("Coś poszło nie tak. Upewnij się, że polecenie jest ustawione poprawnie")

                break


