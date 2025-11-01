import os
import json

CONFIG_FILE = "config.json"


def check_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
    else:
        default_config = {
            "user_saves_folfer": ""
        }
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4)
        return default_config

config = check_config()

print(type(config))
print(config.keys())