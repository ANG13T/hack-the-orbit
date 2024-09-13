from .story_formatter import process_story
from .load_answer import load_answers

from rich.console import Console
import os

console = Console()

def submit_flag():
    user_input = console.input("\nENTER FLAG > ").strip()
    FLAG_1 = load_answers().get('FLAG_1')
    FLAG_2 = load_answers().get('FLAG_2')
    if user_input == FLAG_1:
       process_story('./options/phase_0/complete.txt')
    elif user_input == FLAG_2:
        process_story('./options/phase_1/complete.txt')
    else:
        process_story('./options/submit_flag_error.txt')