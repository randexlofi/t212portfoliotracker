import configparser
import os

config_file = "config.ini"
config = configparser.ConfigParser()

# Create a default file or read the content from it.
def main():
    if not os.path.exists(config_file):
        config['Default'] = {
            't212_key': "KEY_HERE",
        }
        config['Settings'] = {
            'api_request_delay': 5,
            'auto_update_delay': 3600,
            'can_auto_update': True,
            'theme': 'Dark Theme',
        }
        config['Dividends'] = {
            'month': '2, 3, 4, 5',
            'value': '161.17, 172.41, 221.91, 260.38'
        }
        print(f"Config file '{config_file}' generated.")
    else:
        config.read(config_file)
        print(f"Config file '{config_file}' loaded.")
    
    upd_crt_cfg_file()

# Update or create the config file.
def upd_crt_cfg_file():
    with open(config_file, 'w') as cfgfile:
        config.write(cfgfile)
        print("Default config file created/updated.")

def get_data(section, item_id):
    return config[section][item_id]

def update_data(section, item_id, new_data):
    config[section][item_id] = new_data
    upd_crt_cfg_file()


if __name__ == '__main__':
     main()


