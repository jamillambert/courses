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
        options = []
        for i in range(len(incorrect_answers)+1):
            options.append(f"{i+1}. ")
        random.shuffle(options)
        options[0] += self.answer
        self.answer = options[0]
        for i in range(len(incorrect_answers)):
            options[i+1] += incorrect_answers[i]
        options.sort()
        print(options)
        print("##########")
        self.multiple_choice = options
        
        
    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


    def valid_answer(self, user_answer):
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