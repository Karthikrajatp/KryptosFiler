import os
import directory_tree
from rich import print
from rich.prompt import Prompt
from encdec import encrypt
from encdec import decrypt
from panel import displayMenu
from config import *
from efd import listEncryptedFiles
from sounds import *
import time



def clearScreen():
    if (os.name == "nt"):
        os.system("cls")
    elif (os.name == "posix"):
        os.system("clear")
    else:
        print("\nUnknown operating system. Please run this script on a Windows or Linux machine.")
        error()





def main():
    create_config_directory()
    create_config_file()
     
    displayText = """                                                                                                                                             
                                                                       
 █████   ████                                 █████                    
░░███   ███░                                 ░░███                     
 ░███  ███    ████████  █████ ████ ████████  ███████    ██████   █████ 
 ░███████    ░░███░░███░░███ ░███ ░░███░░███░░░███░    ███░░███ ███░░  
 ░███░░███    ░███ ░░░  ░███ ░███  ░███ ░███  ░███    ░███ ░███░░█████ 
 ░███ ░░███   ░███      ░███ ░███  ░███ ░███  ░███ ███░███ ░███ ░░░░███
 █████ ░░████ █████     ░░███████  ░███████   ░░█████ ░░██████  ██████ 
░░░░░   ░░░░ ░░░░░       ░░░░░███  ░███░░░     ░░░░░   ░░░░░░  ░░░░░░  
                         ███ ░███  ░███                                
                        ░░██████   █████                               
                         ░░░░░░   ░░░░░                                
 ███████████  ███  ████                                                
░░███░░░░░░█ ░░░  ░░███                                                
 ░███   █ ░  ████  ░███   ██████  ████████                             
 ░███████   ░░███  ░███  ███░░███░░███░░███                            
 ░███░░░█    ░███  ░███ ░███████  ░███ ░░░                             
 ░███  ░     ░███  ░███ ░███░░░   ░███                                 
 █████       █████ █████░░██████  █████                                
░░░░░       ░░░░░ ░░░░░  ░░░░░░  ░░░░░                                 
                                                                                                                                                       
                                                                       """
    print(f"[green]{displayText}[/green]")
    print("\n")
    path = Prompt.ask("[cyan] Enter Path")
    try:
        if path != "":
            if os.path.exists(path):
                os.chdir(path)
            else:
                print("[bright_red] Invalid Path!\n")
                error()
                time.sleep(2)
                return
        else: 
            path = os.getcwd()
    except:
        print( print("[bright_red] Invalid Path!\n"))
        error()
        time.sleep(2)
        return
    print("\n")
    displayMenu(path)

    while True:
        choice = Prompt.ask("[cyan] Enter your choice [/]")
        if choice == "1":
            print("\n")
            encrypt()
        elif choice == "2":
            print("\n")
            decrypt()
        elif choice == "3":
            print("\n")
            directory_tree.display_tree(path)
            print("\n")
            displayMenu(path)
        elif choice == "4":
            listEncryptedFiles()
            print("\n")
            displayMenu(path)
        elif choice == "5":
            print("\n[bright_red bold] Exiting... [/]")
            break
        else:
            print("\n[bright_red bold] Invalid Choice! [/]")
            error()
            clearScreen()
            displayMenu(path)

     
                                                                                                                                                       
                                                                                                           
                                                                                                           
main()                                                                                                      
                                                                                                        
                                                                 
                                                                                                                                                                                               
                                                                                                                                  
