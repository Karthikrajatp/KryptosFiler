from rich import print
from rich.panel import Panel



def displayMenu(path):
    displayText = f""" [bright_white bold] Current Working Directory \U0001F4C1 :[/bright_white bold] [bright_yellow bold] {path} [/bright_yellow bold] \n\n [bright_red bold] < 1 > [bright_white bold] Encrypt \U0001F510 [/bright_red bold] [bright_blue italic]                    <-   Encrypt a Folder/File! [/bright_blue italic] \n [bright_red bold] < 2 > [bright_white bold] Decrypt \U0001F513 [/bright_red bold] [bright_blue italic]                    <-   Decrypt a Folder/File! [/bright_blue italic] \n [bright_red bold] < 3 > [bright_white bold] List Items \U0001F5DC [/bright_red bold] [bright_blue italic]                  <-   List All Folders/Files in the Directory [/bright_blue italic] \n [bright_red bold] < 4 > [bright_white bold] List Encrypted Items \U0001F441 [/bright_red bold] [bright_blue italic]        <-   List All Encrypted Folders/Files in the System! [/bright_blue italic] \n [bright_red bold] < 5 > [bright_white bold] Exit \U0000274C  [/bright_red bold] [bright_blue italic]                      <-   To Exit the App! [/bright_blue italic] """
    print("")
    print(Panel(displayText, title="[dark_green bold]\U0000269E Main Menu \U0000269F", expand=True, padding=2))
    

