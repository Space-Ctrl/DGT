from qeustion import Question
from quiz_data import question_data
from quiz import quiz
from quiz_ui import QuizInterface
from random import shuffle
import html

# Create a list of Question objects
question_bank = []
# Iterate through the question_data list and create a Question object for each question
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    # Iterate through the incorrect answers and add them to the choices list
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)

# Create a quiz object
quiz = quiz(question_bank)

quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")