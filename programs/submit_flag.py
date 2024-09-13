def submit_flag(flag):
    FLAG_1 = load_answers().get('FLAG_1')
    if flag == FLAG_1:
        print("Flag submitted successfully!")