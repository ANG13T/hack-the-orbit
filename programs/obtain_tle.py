import os

from rich.console import Console
import os

from .story_formatter import process_story
from .load_answer import load_answers

console = Console()

def obtain_tle():
    answer = load_answers()
    CORRECT_SATELLITE = answer.get('SATELLITE_DESIGNATION')
    CORRECT_TLE = answer.get('TLE')
    user_input = console.input("\nENTER SATELLITE DESIGNATION > ").strip()
    if user_input == CORRECT_SATELLITE:
        process_story('./options/phase_0/obtain_tle.txt', placeholders=[user_input, CORRECT_TLE])
    else:
        process_story('./options/phase_0/obtain_tle_error.txt', placeholders=[user_input])