class Quizbrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def next_question(self):
        
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q. {self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_question(self) -> bool:
        if self.question_number >= len(self.question_list):
            return False
        else: 
            return True
        
    def check_answer(self, usr_ans, ans):
        if usr_ans.lower() == ans.lower():
            self.score+=4
            print("Thats right\n")
        else:
            self.score-=1
            print(f"Thats wrong. The correct answer is {ans}\n")
    