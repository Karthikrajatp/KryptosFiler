from rich import print
from rich.console import Console
from rich.table import Table
from config import *

def listEncryptedFiles():
    encryptedFiles = load_config_files()
    if len(encryptedFiles)==0:
        print("\n[bright_red bold] Nothing to Show \U00002639 [/bright_red bold]")
        error()
    else:
        table = Table(title="Encrypted files Database")
        table.add_column("S.No", justify="right", style="cyan", no_wrap=True)
        table.add_column("File/Folder Name", style="magenta")
        table.add_column("Path", justify="right", style="green")
        for i,fileName in enumerate(encryptedFiles):
            table.add_row(str(i+1),fileName,encryptedFiles[fileName])
        console = Console()
        print("\n")
        console.print(table)
            



