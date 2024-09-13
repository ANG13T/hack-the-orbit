from .load_answer import load_answers
from rich.console import Console
from .story_formatter import process_story
import os

console = Console()

def tm_packet_analysis():
     process_story('./options/phase_3/packet_intro.txt')
     command_pass = load_answers().get('COMMAND_MODULE_PASS')
     result = process_binary()
     if result == True:
        process_story('./options/phase_3/packet_dissection.txt', placeholders=[command_pass])
     else:
        console.print("[red]Incorrect binary input! Please try again.[/]")

def process_binary():
    expected_binary = str(load_answers().get('CCSDS_BINARY'))
    binary_lines = expected_binary.strip().split('\n')
    result = True
    for i, line in enumerate(binary_lines, start=1):
        user_input = console.input(f"[bold cyan]Please enter binary line {i}[/bold cyan]: ")
        if user_input.strip() != line.strip():
            console.print(f"[bold red]Error:[/bold red] Incorrect binary input. Expected: {line}")
            result = False
    return result