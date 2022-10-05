import random

class Question:
    def __init__(self, subject, answer_type, difficulty, text, answer):
        self.subject = subject
        self.answer_type = answer_type
        self.difficulty = difficulty
        self.text = text
        self.answer = answer
        self.multiple_choice = []
    
    
    def set_multiple_choice(self, incorrect_answers):
        """Adds the incorrect answers together with the correct answer in a random order into self.multiple_choices[]
        
        All the answers are appended with a sequential number in a random order.  The array is then sorted to have the 
        answers in increasing number"""
        options = []
        for i in range(len(incorrect_answers)+1):
            options.append(f"{i+1}. ")
        random.shuffle(options)
        options[0] += self.answer
        self.answer = options[0]
        for i in range(len(incorrect_answers)):
            options[i+1] += incorrect_answers[i]
        options.sort()
        self.multiple_choice = options
        
        
    def check_answer(self, user_answer):
        """Returns True if user_answer is correct, and False if not"""
        return user_answer.lower() == self.answer.lower()


    def valid_answer(self, user_answer):
        """Returns True if the user_answer is a possible choice for an answer
        
        For true of false questions, any of t, f, true or false are accepted, non case sensitive
        for multiple choice questions the answer must be an integer between 1 and (number of options) inclusive"""
        if self.answer_type == 'boolean':
            if user_answer.lower() in ['t', 'f', 'false', 'true']:
                return True
            else:
                return False
        elif self.answer_type == 'multiple':
            try:
                if int(user_answer) >= 1 and int(user_answer) <= len(self.multiple_choice):
                    return True
                else:
                    return False
            except:
                return False
        elif user_answer != '':
            return True
        else:
            return False
            
    
    def print_question(self):
        """Prints to the terminal the question text"""
        if self.answer_type == 'boolean':
            print(f"True or False {self.text} (T/F)")
        elif self.answer_type == 'multiple':
            print(f"{self.text}")
            for i in range(len(self.multiple_choice)):
                print(f"{self.multiple_choice[i]}")
        else:
            print(f"{self.text}")
