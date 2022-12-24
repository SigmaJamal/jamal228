from random import shuffle, randint
from curses import window
from pickletools import read_unicodestring1
from tkinter.filedialog import askopenfilenames
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel)


app = QApplication([])
btn_OK = QPushButton('Ответить')

lb_Question = QLabel('Самый сложный вопрос в мире!')


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans2.addLayout(layout_ans2)
layout_ans2.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ANsGroupBox = QGroupBox('Р')



def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []
q = Question('Кто придумал цифры?', 'арабы', 'американцы', 'русские', 'индусы')
q1 = Question('Самая быстрая машина в мире?', 'buggati', 'ferrari', 'matiz')
q2 = Question('Какой средний доход человека в америке?','10000$','100000$','143050$','58000$')
def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong_1)
    answer[2].setText(q.wrong_2)
    answer[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

btn_OK.clicked.connect(click_ok)

window.total = 0
window.score = 0

def next_question():
    window.total += 1
    cur_question = randint(0, len(question_list))
    q = question_list[cur_question]
    asq(q)

def check_answer():
    if answer[0].isChecked():
        show_connect('Правильно')
        window.score += 1
    else:
        show_correct('Не правильно')
    print('Задано вопросов:', window.total, 'Верных ответов:', window.score, 'Рейтинг:', window.score/window.total * 100, '%')
    
        


