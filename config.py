import os
import json
from sounds import *


if os.name == "posix":
    config_dir = os.path.expanduser("~/.config/KryptosFiler")
    config_file = os.path.join(config_dir, "config.json")
elif os.name=="nt":
    config_dir = os.path.expanduser("~/AppData/Local/KryptosFiler")
    config_file = os.path.join(config_dir, "config.json")
else:
    raise OSError("\nUnsupported Operating System")
    error()

def create_config_directory():
    os.makedirs(config_dir,exist_ok=True)
def create_config_file():
    if not os.path.exists(config_file):
        with open(config_file,"w") as f:
            json.dump({},f)
def load_config_files():
    if not os.path.exists(config_file):
        return {}
    
    with open(config_file, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_encrypted_file(encrypted_files):
    with open(config_file, "w") as f:
        json.dump(encrypted_files, f)

def add_encrypted_file(path, file_name):
    encrypted_files = load_config_files()
    encrypted_files[file_name] = path
    save_encrypted_file(encrypted_files)

def remove_encrypted_file(path, file_name):
    encrypted_files = load_config_files()
    encrypted_files = {f: p for f, p in encrypted_files.items() if f != file_name or p != path}
    save_encrypted_file(encrypted_files)


