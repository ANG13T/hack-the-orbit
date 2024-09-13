from rich.console import Console
from rich.text import Text
import re

"""
RULES:
- **text** -> should bold the text
- text after [INFO] should be blue
- text after [ERROR] should be red
- text after [ACTION] should be orange
- text after [SUCCESS] should be green
- text after [DATA] should be light purple
"""

# Initialize the rich console
console = Console()

# Function to replace [PLACEHOLDER <number>] with corresponding values from the placeholder array
def replace_placeholders(text, placeholders):
    def replacement(match):
        index = int(match.group(1))  # Extract index number from the placeholder
        if 0 <= index < len(placeholders):
            return placeholders[index]  # Return the placeholder value
        return match.group(0)  # Return the original placeholder if index is out of range

    pattern = r"\[PLACEHOLDER (\d+)\]"
    return re.sub(pattern, replacement, text)

# Function to process and format story text
def process_story(file_path, placeholders=[]):
    with open(file_path, 'r') as file:
        empty_line_count = 0  # Track consecutive empty lines
        for line in file:
            line = line.rstrip()  # Remove trailing spaces and newlines

            # Replace placeholders before formatting
            line = replace_placeholders(line, placeholders)

            # Handle empty lines
            if not line:
                empty_line_count += 1
                if empty_line_count == 1:
                    console.print("")  # Only print one newline for one empty line
                continue
            else:
                empty_line_count = 0  # Reset counter if a non-empty line is found

            # Process special tags and apply formatting
            if "[INFO]" in line:
                formatted_text = format_info(line)
            elif "[DATA]" in line:
                formatted_text = format_data(line)
            elif "[ERROR]" in line:
                formatted_text = format_error(line)
            elif "[ACTION]" in line:
                formatted_text = format_action(line)
            elif "[SUCCESS]" in line:
                formatted_text = format_success(line)
            else:
                formatted_text = format_bold(line)

            # Print the formatted text
            console.print(formatted_text)

# Formatting functions for different tags
def format_info(text):
    return process_bold(Text(text, style="blue"))

def format_error(text):
    return process_bold(Text(text, style="red"))

def format_action(text):
    return process_bold(Text(text, style="orange3"))

def format_success(text):
    return process_bold(Text(text, style="green"))

def format_data(text):
    return process_bold(Text(text, style="purple"))

def format_bold(text):
    # Process **text** to be bold
    return process_bold(Text(text))

# Function to process and apply bold to text within ** **
def process_bold(text_obj):
    pattern = r"\*\*(.*?)\*\*"
    text_str = text_obj.plain
    bold_sections = re.findall(pattern, text_str)

    # Create a new Text object with sections of bold
    new_text = Text()

    # Split the text based on bold patterns
    parts = re.split(pattern, text_str)

    for index, part in enumerate(parts):
        if index % 2 == 1:
            # Odd index: bold section
            new_text.append(part, style="bold")
        else:
            # Even index: regular section
            new_text.append(part, style=text_obj.style)

    return new_text
