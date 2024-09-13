"""
 --- SATELLITE HACKING SEQUENCE CTF ---

          Created by G4LXY
"""

from rich.console import Console
import os

console = Console()

from programs.exit import exit
from programs.help import help
from programs.ls import ls
from programs.cd import cd
from programs.pwd import pwd
from programs.man import man
from programs.help import help
from programs.exit import exit

OPTIONS = [
    ["START CHALLENGE", "ABOUT", "EXIT"]
]

COMMANDS = {
    "ls": {
        "description": "List files in the current directory",
        "function": ls
    },
    "cd": {
        "description": "Change directory",
        "function": cd
    },
    "pwd": {
        "description": "Print the current working directory",
        "function": pwd
    },
    "man": {
        "description": "Display manual pages",
        "function": man
    },
    "help": {
        "description": "List command information",
        "function": help
    },
    "exit": {
        "description": "Exit the program",
        "function": exit
    }
}

# DISPLAY FUNCTIONS

def banner():
    f = open('banner.txt', 'r')
    file_contents = f.read()
    console.print("\n [cyan]" + file_contents + "[/]")
    f.close()

def display_options(index):
    row = OPTIONS[index]
    for i in range(len(row)):
        console.print(f"{' ' * 10}[cyan]{i + 1}. {row[i]}\n[/]")

def init_intro():
    banner()

def retrieve_input(options_index):
    user_input = console.input("ENTER YOUR CHOICE: ")
    try:
        user_input = int(user_input)
        if user_input > 0 and user_input <= len(OPTIONS[options_index]):
            return user_input
        else:
            console.print("[red]Invalid option! Please try again.[/]")
            return retrieve_input(options_index)
    except ValueError:
        console.print("[red]Invalid option! Please try again.[/]")
        return retrieve_input(options_index)

def read_contents(path):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, path)
    f = open(file_name, 'r')
    file_contents = f.read()
    console.print("\n[cyan]" + file_contents + "[/]")
    f.close()

# CHALLENGE FUNCTIONS

def command_prompt():
    while True:
        command = console.input("\nENTER COMMAND > ").strip().lower()
        if command == "exit":
            console.print("[red]Exiting the program...[/]")
            break
        result = interpret_command(command)
        console.print(result)

def start_challenge():
    read_contents('./options/welcome.txt')
    command_prompt()

def about():
    read_contents('./options/about.txt')

def interpret_command(command):
    cmd_info = COMMANDS.get(command)
    if cmd_info:
        func = cmd_info["function"]
        return func()
    else:
        return "Unknown command! Type 'help' for a list of commands."

# TEXT PROCESSING FUNCTIONS:
def text_processing(txt_path, placeholder):
    pass

# OPTION DICTIONARY

start_challenge = {
    0: start_challenge,
    1: about,
    2: exit
}

if __name__ == "__main__":
    init_intro()
    display_options(0)
    choice = retrieve_input(0)
    start = start_challenge.get(choice - 1, None)
    start()