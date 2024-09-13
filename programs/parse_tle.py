from rich.console import Console
from rich.text import Text

console = Console()

def parse_tle():
    line_1 = console.input("Enter Line 1 of the TLE data: ").strip()
    line_2 = console.input("Enter Line 2 of the TLE data: ").strip()

    # Validate input (basic check)
    if len(line_1) < 69 or len(line_2) < 69:
        console.print("[red]Error: Input lines are too short to be valid TLE data.[/red]")
        return

    satellite_number = line_1[2:7].strip()
    classification = line_1[7:8].strip()
    international_designator = line_1[9:17].strip()
    epoch = line_1[18:32].strip()
    decay_rate = line_1[33:43].strip()

    inclination = line_2[8:16].strip()
    right_ascension = line_2[17:25].strip()
    eccentricity = line_2[26:33].strip()
    argument_of_perigee = line_2[34:42].strip()
    mean_anomaly = line_2[43:51].strip()
    mean_motion = line_2[52:63].strip()

    console.print("\n[bold cyan]TLE Orbital Characteristics[/bold cyan]")
    console.print(f"[bold]Satellite Number:[/bold] {satellite_number}")
    console.print(f"[bold]Classification:[/bold] {classification}")
    console.print(f"[bold]International Designator:[/bold] {international_designator}")
    console.print(f"[bold]Epoch:[/bold] {epoch}")
    console.print(f"[bold]Decay Rate:[/bold] {decay_rate}")
    console.print(f"[bold]Inclination:[/bold] {inclination} degrees")
    console.print(f"[bold]Right Ascension:[/bold] {right_ascension} degrees")
    console.print(f"[bold]Eccentricity:[/bold] {eccentricity}")
    console.print(f"[bold]Argument of Perigee:[/bold] {argument_of_perigee} degrees")
    console.print(f"[bold]Mean Anomaly:[/bold] {mean_anomaly} degrees")
    console.print(f"[bold]Mean Motion:[/bold] {mean_motion} rev/day")
