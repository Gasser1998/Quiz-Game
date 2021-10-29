from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(text1=question_text,answer1=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() is True:
    quiz.next_question()

print('Quiz complete')
print(f'Your score is {quiz.score}/{len(question_bank)}.')
