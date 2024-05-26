import configparser
#Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read("config.ini")
for i in config_obj:
    print(i)