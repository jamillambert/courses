from html_parser import parse_site
from quiz import Quiz
from os import system


def input_number(text, min_number, max_number, default):
    """Returns a number input from the terminal or default if it fails
    
    The input text is displayed to the terminal as a prompt for the user to input
    a number.  If a number is not entered within the input min and max values the
    default value is returned"""
    try:
        number = int(input(text))
    except ValueError:
        number = min_number - 1  # Invalid int entered so this forces if statement below to be true
    if number < min_number or number > max_number:
        input(f"invalid input, set to default {default}, press enter to continue")
        number = default
    return number


def input_text(text, default):
    """Returns either the text in the default array if it is entered or it's index, otherwise the text at index 0 is returned
    
    The input text is displayed to the terminal as a prompt for the user to input
    the index or text of the array."""
    return_text = 'invalid'
    choice = input(text)
    try:
        number = int(choice) - 1
        return_text = default[number]
    except ValueError:
        for d in default:
            if choice == d:
                return_text = d
    if return_text == 'invalid':
        return_text = default[0]
        input(f"invalid input, set to default {return_text}, press enter to continue")
    return return_text


def set_defaults(quiz):
    """Sets the quiz variables to their default values"""
    quiz.num_questions = 10
    quiz.subject = 9
    quiz.difficulty = 'medium'
    quiz.question_type = ''


def main_menu(quiz):
    """Displays a settings menu where the user can change the quiz settings"""
    options = {'n': 'Change the number of questions', 'd': 'Change the difficulty', 't': 'Change the question type',
               's': 'Change the question subject', 'r': 'Reset to default values', 'x': 'Save and exit settings'}
    choice = 'uninitialised'
    while choice != 'x':
        system('cls||clear')
        print_options(quiz)
        print(
            "\n\033[1;36mSettings\033[0m\nEnter the letter corresponding to the setting you want to change")
        for key in options:
            print(f"'{key}': {options[key]}")
        choice = input(":")
        if choice == 'n':
            quiz.num_questions = input_number(
                '\nEnter the number of questions: (1 to 20) ', 1, 20, 10)
        elif choice == 'd':
            quiz.difficulty = input_text('\nEnter the difficulty, 1: easy, 2: medium, 3: hard : ', [
                'easy', 'medium', 'hard'])
        elif choice == 't':
            quiz.question_type = input_text(
                '\nEnter the question type, 1: True/False, 2: Multiple Choice, 3: All Questions : ',
                ['boolean', 'multiple', ''])
        elif choice == 's':
            print("\nChoose a subject number from the below list:")
            code_list = []
            for key in quiz.categories:
                print(f"'{key}': {quiz.categories[key]}")
                code_list.append(key)
            quiz.subject = input_number(
                'Subject number: ', min(code_list), max(code_list), min(code_list))
        elif choice == 'r':
            set_defaults(quiz)


def print_options(quiz):
    """Prints to the terminal the current settings of the quiz"""
    type_text = ''
    if quiz.question_type == 'boolean':
        type_text = 'True or False '
    elif quiz.question_type == 'multiple':
        type_text = 'multiple choice '
    print(
        f"Selected options are: \033[1m{quiz.num_questions} {quiz.difficulty} {type_text}questions on {quiz.categories[quiz.subject]}\033[0m")


def new_game():
    """Creates a new Quiz object, sets the defaults and prompts the user to change settings or keep defaults"""
    quiz = Quiz()
    set_defaults(quiz)
    system('cls||clear')
    print(("\n\n\033[1;36mWelcome to the Trivia Quiz\033[0m\n\n"))
    print("Questions are sourced from Open Trivia Database https://opentdb.com/")
    print_options(quiz)
    choice = input("\nPress Enter to continue, or type 's' to change settings: ")
    if choice == 's':
        main_menu(quiz)
    print("Sourcing questions from https://opentdb.com/")
    quiz.create_question_list()
    return quiz


def main():
    """Starts a new quiz, when finished the users is asked to start again or exit"""
    while True:
        quiz = new_game()

        system('cls||clear')
        for i in range(quiz.num_questions):
            quiz.ask_question(i)

        print(
            f"\n\033[1mYour final score was {quiz.score}/{quiz.question_number}\033[0m\n\n")
        choice = input("Do you want to play again? (Y/N) ").lower()
        if choice == 'y':
            continue
        else:
            break


main()
