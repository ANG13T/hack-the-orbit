"""
 --- SATELLITE HACKING SEQUENCE CTF ---

          Created by G4LXY
"""

from rich.console import Console
import os

console = Console()

from programs.help import help
from programs.ls import ls
from programs.pwd import pwd
from programs.help import help
from programs.story_formatter import process_story
from programs.obtain_tle import obtain_tle
from programs.parse_tle import parse_tle
from programs.submit_flag import submit_flag
from programs.rx_suite import rx_suite
from programs.tm_packet_analysis import tm_packet_analysis
from programs.satellite_command_module import satellite_command_module
from programs.subsystem_status import subsystem_status

OPTIONS = [
    ["START CHALLENGE", "ABOUT", "EXIT"]
]

COMMANDS = {
    "ls": {
        "description": "List files in the current directory",
        "function": ls
    },
    "pwd": {
        "description": "Print the current working directory",
        "function": pwd
    },
    "help": {
        "description": "List command information",
        "function": help
    },
    "obtain_tle": {
        "description": "Obtain TLE",
        "function": obtain_tle
    },
    "./obtain_tle": {
        "description": "Obtain TLE",
        "function": obtain_tle
    },
    "parse_tle": {
        "description": "Parse Orbital Characteristics from TLE",
        "function": parse_tle
    },
    "./parse_tle": {
        "description": "Parse Orbital Characteristics from TLE",
        "function": parse_tle
    },
    "subsystem_status": {
        "description": "Obtain subsystem status information",
        "function": subsystem_status
    },
    "./subsystem_status": {
        "description": "Obtain subsystem status information",
        "function": subsystem_status
    },
    "rx_suite": {
        "description": "Ground Station RX Suite",
        "function": rx_suite
    },
    "./rx_suite": {
        "description": "Ground Station RX Suite",
        "function": rx_suite
    },
    "tm_packet_analysis": {
        "description": "TM Packet Analysis Suite",
        "function": tm_packet_analysis
    },
    "./tm_packet_analysis": {
        "description": "TM Packet Analysis Suite",
        "function": tm_packet_analysis
    },
    "satellite_command_module": {
        "description": "Satellite Uplink Command Module",
        "function": satellite_command_module
    },
    "./satellite_command_module": {
        "description": "Satellite Uplink Command Module",
        "function": satellite_command_module
    },
    "submit_flag": {
        "description": "Submit Flag Attempt",
        "function": submit_flag
    },
    "./submit_flag": {
        "description": "Submit Flag Attempt",
        "function": submit_flag
    },
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
    process_story(file_name)

# CHALLENGE FUNCTIONS

def command_prompt():
    while True:
        command = console.input("\nENTER COMMAND > ").strip().lower()
        if command == "exit":
            console.print("[red]Exiting the program...[/]")
            break
        interpret_command(command)

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