import main_window
import process_command as pc

if __name__ == "__main__":
    print("Uruchamianie...")
    commandProcessing = pc.CommandProcessing()
    main_window.buildApp(commandProcessing)