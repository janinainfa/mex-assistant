import main_window
import process_command as pc
import os
import create_config

if __name__ == "__main__":
    print("Uruchamianie...")
    try:
        open(os.path.expanduser("~") + "/mexassistant/config.ini")
    except:
        create_config.createConfig()
    commandProcessing = pc.CommandProcessing()
    main_window.buildApp(commandProcessing)