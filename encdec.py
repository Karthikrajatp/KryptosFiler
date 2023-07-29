import os
import stdiomask
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from directory_tree import display_tree
from rich.prompt import Prompt
from rich import print
import subprocess
from config import *
from sounds import *



salt = b"\x7fB \xd3:\xb3\x94\xf6\xf0NO\xba\x7fH\\\xfe"


def encrypt():
    target = Prompt.ask("[cyan] Enter Folder/File Name [/]")
    print("")
    if not os.path.exists(target):
        print("\n[bright_red bold] Target does not exist in the current working directory!\n [/]")
        warning()
    else:
        try:
            if "." not in target:
                display_tree(target)
                print("\n")
        except:
            print("[bright_red bold] Invalid Target!\n [/]")
            warning()
            return
        password = stdiomask.getpass(prompt=" Enter Password:",mask="•")
        print("")
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),salt=salt,iterations=500000,length=32)
        try:
            subprocess.run(["zip", "-r", "-q", target + ".zip", target])
            subprocess.run(["rm","-rf",target])
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
            fernet_obj = Fernet(key)
            with open(f"{target}.zip","rb") as file:
                data = file.read()
            encrypted_data = fernet_obj.encrypt(data)
            with open(f".{target}","wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
            print("\n[bright_green bold] Encrypted Successfully! [/]\n")
            success()
            target_path = os.getcwd()
            add_encrypted_file(target_path,target)
            subprocess.run(["rm","-rf",target+".zip"])
        except Exception as e:
            print(f"\n[bright_red bold] An Error Ocurred:{str(e)}\n")
            warning()



def decrypt():
    target = Prompt.ask("[cyan] \n Enter Folder/File Name [/]")
    password = stdiomask.getpass(prompt=" Enter Password:",mask="•")
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),salt=salt,iterations=500000,length=32)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    try:
        with open(f".{target}","rb") as file:
            data = file.read()
    except:
        print("\n[bright_red bold]Folder/File not found![/]")
        warning()
        return
    fernet_obj = Fernet(key)
    try:
        decrypted = fernet_obj.decrypt(data)
    except:
        print("\n[bright_red bold]Wrong password![/]")
        error()
        return
    try:
        with open(f"{target}.zip","wb") as decrypted_file:
            decrypted_file.write(decrypted)
        subprocess.run(["unzip", "-q", target + ".zip"])
        subprocess.run(["rm","-rf",target+".zip"])
        print("\n[bright_green bold] Decrypted Successfully! [/]\n")
        success()
        target_path = os.getcwd()
        remove_encrypted_file(target_path,target)
        subprocess.run(["rm","-rf","."+target])
        if "." not in target:
            subprocess.run(["open", target])
    except Exception as e:
        print(f"\n[bright_red bold] An Error Occured : {str(e)}[/]")
        warning()







