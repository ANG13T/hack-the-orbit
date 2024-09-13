import yaml
import os

def load_answers():
    file_path = 'ANSWERS.yaml'
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, file_path)
    try:
        with open(file_path, 'r') as file:
            answers = yaml.safe_load(file)
            return answers
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"[ERROR] Error parsing YAML file: {e}")
        return None