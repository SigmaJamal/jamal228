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
