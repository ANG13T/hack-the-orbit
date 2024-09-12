"""
 --- SATELLITE HACKING SEQUENCE CTF ---

          Created by G4LXY
"""

from rich.console import Console
import os

console = Console()

OPTIONS = [
    ["START CHALLENGE", "ABOUT", "EXIT"]
]

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

# CHALLENGE FUNCTIONS

def start_challenge():
    pass

def about():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, './options/about.txt')
    f = open(file_name, 'r')
    file_contents = f.read()
    console.print("\n[cyan]" + file_contents + "[/]")
    f.close()

def exit():
    print("Exiting program...")
    os._exit(0)


# OPTION DICTIONARY

switch = {
    0: start_challenge,
    1: about,
    2: exit
}

if __name__ == "__main__":
    init_intro()
    display_options(0)
    choice = retrieve_input(0)
    func = switch.get(choice - 1, None)
    func()
