class QuizBrain:
    
    
    def __init__(self, question_list, number_questions): 
        self.question_number = 0
        self.score = 0
        self.number_questions = number_questions
        self.question_list = question_list
        
        
    def ask_question(self, index):
        current_question = self.question_list[index]
        while True:
            user_answer = input(f"\n\nQ.{index+1}: {current_question.text} (True/False): ").lower()
            if current_question.valid_answer(user_answer):
                break
            else:
                print("Invalid answer, type t for true, f for false or the number option for multiple choice")

        self.print_result(user_answer, current_question)
    

    def print_result(self, user_answer, question):
        if question.answer_type == 'boolean' or question.answer_type == 'multiple':
            correct = user_answer[0].lower() == question.answer[0].lower()
        else:
            correct = user_answer.lower() == question.answer.lower()
        if correct:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect")
        print(f"The correct answer was: {question.answer}")
        print(f"You current score is {self.score}/{self.question_number}")