#Quiz Class
class quiz:
    #Constructor
    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None
    #Method to check if there are more questions
    def has_more_questions(self):
        
        return self.question_no < len(self.questions)
    #Method to get the next question
    def next_question(self):
        
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"
    #Method to check if the answer is correct
    def check_answer(self, user_answer):       
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
    #Method to get the score
    def get_score(self):
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)