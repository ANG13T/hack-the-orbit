import os
from rich.console import Console

console = Console()

def ls():
    programs = ['obtain_tle', 'parse_tle', 'subsystem_status', 'rx_suite', 'tm_packet_analysis', 'satellite_command_module', 'submit_flag']
    program_text = "  ".join(programs)
    console.print("\n[blue]" + program_text + "[/]")