class QuizBrain:

    def __init__(self, question_list):
        self.q_number = 0
        self.score = 0
        self.q_list = question_list


    def still_has_questions(self):
         if self.q_number < len(self.q_list):
             return True
         else:
            return False

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it rigth!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}")

