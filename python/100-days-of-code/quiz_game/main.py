import random, re
from question_model import Question
from quiz_brain import QuizBrain
from html_parser import parse_site

 
def new_game():
    question_bank = []
    print(("Welcome to the true false quiz"))
    print("Questions are sourced from Open Trivia Database https://opentdb.com/")
    #difficulty = input("Enter the difficulty (1:Easy, 2:Medium or 3:Hard").lower()
    open_trivia = parse_site("https://opentdb.com/api.php?amount=10&category=17&type=boolean")
    question_bank = parse_open_trivia(open_trivia)
    # if difficulty == '1' or difficulty == 'easy':
    #     for q in question_data_easy:
    #         question_bank.append(Question(q["text"], q["answer"]))
    # if difficulty == '2' or difficulty == 'medium':
    #     for q in question_data_medium:
    #         question_bank.append(Question(q["text"], q["answer"]))
    # if difficulty == '3' or difficulty == 'hard':
    #     for q in question_data_hard:
    #         question_bank.append(Question(q["text"], q["answer"]))
    return question_bank


def parse_open_trivia(raw_text):
    # The following characters need to be escaped in the split function . \ + * ? [ ^ ] $ ( ) { } = !  | : -
    raw_questions = re.split('\,{', raw_text)
    questions = []
    for i in range(len(raw_questions)):
        # Remove the leading " from the text
        parsed_question = raw_questions[i].strip('"')
        # Split the text into a list delimited by (including the quotes) "," | ":" | ":[" | "]}]} | "]}
        parsed_question = re.split("\",\"|\"\:\"|\"\:\[\"|\"\]\}\]\}|\"\]\}", parsed_question)
        # take out the required parts of the question list, [7] is the question text and [9] is the answer
        subject = parsed_question[1]
        answer_type = parsed_question[3]
        difficulty = parsed_question[5]
        text = parsed_question[7]
        answer = parsed_question[9]
        question = Question(subject, answer_type, difficulty, text, answer)
        if answer_type != 'boolean':
            incorrect_answers = []
            for i in range(11, len(parsed_question)-1):
                incorrect_answers.append(parsed_question[i])        
            question.set_multiple_choice(incorrect_answers)
        questions.append(question)
    return questions

num_questions = 10                  
question_bank = new_game()
random.shuffle(question_bank)
quiz = QuizBrain(question_bank, num_questions)
for i in range(num_questions):
    quiz.ask_question(i)

print(f"\n\033[1mYour final score was {quiz.score}/{quiz.question_number}\033[0m\n\n")
