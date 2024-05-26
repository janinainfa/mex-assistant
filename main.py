import window
import voice_operations as vo
import process_command as pc

if __name__ == "__main__":
    vo.speak("Dzień dobry")
    commandProcessing = pc.CommandProcessing()
    window.buildApp(commandProcessing)