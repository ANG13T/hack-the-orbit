from .load_answer import load_answers
from rich.console import Console
from .story_formatter import process_story
import os

console = Console()

def tm_packet_analysis():
     process_story('./options/phase_3/packet_intro.txt')
     result = process_binary()
     if result == True:
        process_story('./options/phase_3/packet_dissection.txt')
     else:
        console.print("[red]Incorrect binary input! Please try again.[/]")

def process_binary():
    expected_binary = load_answers().get('CCSDS_BINARY')
    for i, expected_binary in enumerate(binary_lines, start=1):
        user_input = console.input(f"[bold cyan]Please enter binary line {i}[/bold cyan]: ")

        if user_input != expected_binary:
            console.print(f"[bold red]Error:[/bold red] Incorrect binary input. Expected: {expected_binary}")
            return False
    return True