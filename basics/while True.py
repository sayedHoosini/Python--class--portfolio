while True:
    score_input = input("Enter the student's score (or type 'exit' to quit): ")
    if score_input.lower() == 'exit':
        print("Exiting the grading program.")
        break
    try:
        score = float(score_input)
        if 0 <= score <= 100:
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"
            print(f'Your grade is {grade}')
        else:
            print(f'{score} is an invalid test score')
    except ValueError:
        print("Please enter a valid numeric score or 'exit'.")
