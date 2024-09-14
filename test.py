from programs.load_answer import load_answers

def load():
    answers = load_answers()
    print(answers)
    CORRECT_SATELLITE = answers.get('SATELLITE_DESIGNATION')
    print(CORRECT_SATELLITE)


load()