from .load_answer import load_answers
from rich.console import Console
from .story_formatter import process_story
import os

console = Console()

def rx_suite():
    user_input = console.input("\nPASSWORD REQUIRED > ").strip()
    PSWD = load_answers().get('PSWD')

    if user_input == PSWD:
        process_story('./options/phase_2/complete.txt')

        process_story('./options/phase_2/rx_suite_options.txt')

        input_command = console.input("\nRX SUITE > ").strip()

        process_command(input_command)

    else:
        console.print("[red]Incorrect password! Please try again.[/]")

def process_command(command):
    segments = command.split(" ")
    command = segments[0]

    if command == "record_signal":
        record(segments[1])
    elif command == "demod":
        demodulate(segments[1])
    elif command == "decrypt":
        decrypt(segments[1])

def record(freq):
    FQCY_RANGE_START = int(load_answers().get('FQCY_RANGE').split('-')[0])
    FQCY_RANGE_END = int(load_answers().get('FQCY_RANGE').split('-')[1])
    SIGNAL_PATH = load_answers().get('SIGNAL_PATH')

    freq_input = int(freq)

    if freq_input > FQCY_RANGE_START and freq_input < FQCY_RANGE_END:
        process_story('./options/phase_2/rx_suite_record.txt', placeholders=[str(freq_input), SIGNAL_PATH])
    else:
        console.print("[red]Invalid frequency! Please try again.[/]")

def demodulate(wav_file):
    SIGNAL_PATH = load_answers().get('SIGNAL_PATH')
    BIN_PATH = load_answers().get('BIT_STREAM_PATH')
    AES = load_answers().get('AES')
    if wav_file == SIGNAL_PATH:
        MOD_INDEX = load_answers().get('MOD_INDEX')
        modulation_options = ['AM', 'FM', 'SSB', 'DSB', 'PSK']

        console.print("\nMODULATION OPTIONS:")
        for i, option in enumerate(modulation_options):
            console.print(f"{i + 1}. {option}")

        mod_type = int(console.input("\nENTER MODULATION TYPE > ").strip()) - 1

        if mod_type == MOD_INDEX:
            process_story('./options/phase_2/rx_suite_demod.txt', placeholders=[SIGNAL_PATH, modulation_options[MOD_INDEX], BIN_PATH, AES])
    else:
        console.print("[red]Invalid signal file! Please try again.[/]")

def decrypt(bin_file):
    BIN_PATH = load_answers().get('BIT_STREAM_PATH')
    AES = load_answers().get('AES')
    CCSDS_BINARY = load_answers().get('CCSDS_BINARY')
    if bin_file == BIN_PATH:
        key = console.input("\nENTER AES-128 KEY > ").strip()

        if key == AES:
            process_story('./options/phase_2/complete.txt', placeholders=[key, CCSDS_BINARY])
       else:
            console.print("[red]Invalid key! Please try again.[/]")
    else:
        console.print("[red]Invalid binary file! Please try again.[/]")