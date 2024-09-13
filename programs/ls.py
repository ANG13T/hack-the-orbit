import os
from rich.console import Console

console = Console()

def ls():
    programs = ['obtain_tle', 'parse_tle']
    program_text = "  ".join(programs)
    console.print("\n[blue]" + program_text + "[/]")