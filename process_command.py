from voice_operations import *

class CommandProcessing():
    def __init__(self):
        pass

    def processCommand(self, window):
        command = takeVoice(3, window)
        window.stateLabel.setText(command)
