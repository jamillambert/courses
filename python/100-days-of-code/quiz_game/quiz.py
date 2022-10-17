import random
import re

from html_parser import parse_site
from question_model import Question


class Quiz:

    def __init__(self):
        self.num_questions = 10
        self.subject = 9
        self.difficulty = 'medium'
        self.question_type = ''
        self.score = 0
        self.question_number = 0
        self.question_list = []
        self.categories = {9: 'General Knowledge', 10: 'Books', 11: 'Film', 12: 'Music', 13: 'Musicals & Theatres', 14: 'Television', 15: 'Video Games',
                           16: 'Board Games', 17: 'Science & Nature', 18: 'Computers', 19: 'Mathematics', 20: 'Mythology', 21: 'Sports', 22: 'Geography',
                           23: 'History', 24: 'Politics', 25: 'Art', 26: 'Celebrities', 27: 'Animals', 28: 'Vehicles', 29: 'Comics', 30: 'Gadgets',
                           31: 'Anime & Manga', 32: 'Cartoons and Animations'}


    def ask_question(self, index):
        """Prints out the next question and checks if the answer is correct"""
        self.question_number += 1
        current_question = self.question_list[index]
        while True:
            print("\n")
            current_question.print_question()
            user_answer = input(f"\nQ.{index+1}: Answer? ").lower()
            if current_question.valid_answer(user_answer):
                break
            else:
                print(
                    "Invalid answer, type t for true, f for false or the number option for multiple choice")
        self.print_result(user_answer, current_question)
        

    def create_question_list(self):
        """Creates a question list from the api on https://opentdb.com
        
        the url required is built using self.build_url() with the values for the number of questions, subject, 
        difficulty and question type.
        The text returned by the api is then parsed html_paresr then then by self.parse_open_trivia()"""
        url = self.build_url(self.num_questions,
                             self.subject, self.difficulty, self.question_type)
        raw_text = parse_site(url)
        self.question_list = self.parse_open_trivia(raw_text)
        random.shuffle(self.question_list)
        
        
    def print_result(self, user_answer, question):
        """Prints to the terminal the result of question and answer input
        
        If the answer is correct the score is incremented by 1"""
        if question.answer_type == 'boolean' or question.answer_type == 'multiple':
            correct = user_answer[0].lower() == question.answer[0].lower()
        else:
            correct = user_answer.lower() == question.answer.lower()
        if correct:
            self.score += 1
            print("\033[0;32mCorrect!\033[0m")
        else:
            print("\033[0;31mIncorrect\033[0m")
        print(f"The correct answer was: {question.answer}")
        print(f"You current score is {self.score}/{self.question_number}")


    def build_url(self, num_questions, subject, difficulty, question_type):
        """Builds the url for the opentdb api using the input variables"""
        url = "https://opentdb.com/api.php?"
        url += f"amount={num_questions}&"
        url += f"category={subject}&"
        url += f"difficulty={difficulty}&"
        url += f"type={question_type}"
        return url


    def parse_open_trivia(self, raw_text):
        """Returns an array of questions by extracting the question elements from the text input from the opentdb.com api
        
        The text is all enclosed in quotations, but so is some text within an element
        therefore the delimiters used are multicharacters such as quote comma quote."""
        # The following characters need to be escaped in the split function . \ + * ? [ ^ ] $ ( ) { } = !  | : -
        raw_questions = re.split('\,{', raw_text)
        questions = []
        for i in range(len(raw_questions)):
            # Remove the leading " from the text
            parsed_question = raw_questions[i].strip('"')
            # Split the text into a list delimited by (including the quotes) "," | ":" | ":[" | "]}]} | "]}
            parsed_question = re.split(
                "\",\"|\"\:\"|\"\:\[\"|\"\]\}\]\}|\"\]\}", parsed_question)
            # take out the required parts of the question list, [7] is the question text and [9] is the answer
            subject = parsed_question[1]
            answer_type = parsed_question[3]
            difficulty = parsed_question[5]
            text = parsed_question[7]
            answer = parsed_question[9]
            question = Question(subject, answer_type, difficulty, text, answer)
            if answer_type != 'boolean':
                multiple_choices = []
                for i in range(11, len(parsed_question)-1):
                    multiple_choices.append(parsed_question[i])
                question.set_multiple_choice(multiple_choices)
            questions.append(question)
        return questions
