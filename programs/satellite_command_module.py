from .load_answer import load_answers
from rich.console import Console
from .story_formatter import process_story
import os

console = Console()

def satellite_command_module():
    user_input = console.input("\nPASSWORD REQUIRED > ").strip()
    COMMAND_MODULE_PASS = load_answers().get('COMMAND_MODULE_PASS')

    if user_input == PSWD:
        process_story('./options/phase_4/satellite_command_module.txt')

    else:
        console.print("[red]Incorrect password! Please try again.[/]")
