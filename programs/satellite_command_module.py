from .load_answer import load_answers
from rich.console import Console
from .story_formatter import process_story
import os

console = Console()

def satellite_command_module():
    user_input = console.input("\nPASSWORD REQUIRED > ").strip()
    COMMAND_MODULE_PASS = load_answers().get('COMMAND_MODULE_PASS')

    if user_input == COMMAND_MODULE_PASS:
        process_story('./options/phase_4/satellite_command_module.txt')

        result = process_binary()

        if result == True:
            process_story('./options/final/final.txt')
        else:
            console.print("[red]Incorrect command injection attempt! Please try again.[/]")

    else:
        console.print("[red]Incorrect password! Please try again.[/]")

# TODO: check that power override is 0x01 and Power Level > 50dBm by analyzing the binary
def process_binary():
    injection_bin = load_answers().get('COMMAND_INJECTION_BIN')
    binary_lines = injection_bin.strip().split('\n')
    result = True
    for i, line in enumerate(binary_lines, start=1):
        user_input = console.input(f"[bold cyan]Please enter binary line {i}[/bold cyan]: ")
        if user_input.strip() != line.strip():
            console.print(f"[bold red]Error:[/bold red] Incorrect binary input. Expected: {line}")
            result = False
    return result