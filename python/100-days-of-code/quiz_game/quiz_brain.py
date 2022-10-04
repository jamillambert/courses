class QuizBrain:
    
    
    def __init__(self, question_list, number_questions) -> None: 
        self.question_number = 0
        self.score = 0
        self.number_questions = number_questions
        self.question_list = question_list
        
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"\n\nQ.{self.question_number}: {current_question[0]} (True/False): ").lower()
            if user_answer == 't' or user_answer == 'true':
                user_answer = 'True'
                break
            elif user_answer == 'f' or user_answer == 'false':
                user_answer = 'False'
                break
            else:
                print("Invalid input, enter True or False, or t or f")
        self.check_answer(user_answer, current_question[1])
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The correct answer was: {correct_answer}")
        print(f"You current score is {self.score}/{self.question_number}")