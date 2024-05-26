import configparser
import re
import subprocess

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
        command = command.lower()
        self.loadConfig()
        for i in self.config:
            if re.search(i, command):
                if self.config[i]["type"] == "command_line":
                    subprocess.Popen(self.config[i]["command"])
                if self.config[i]["type"] == "python":
                    exec(self.config[i]["command"])


