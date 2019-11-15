from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
import random

class Ui_Okay(QtWidgets.QWidget):

    def setupUi(self, Okay):
        Okay.setObjectName("Okay")
        Okay.resize(480, 800)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack1 = QtWidgets.QWidget()
        self.stack2 = QtWidgets.QWidget()
        self.stack3 = QtWidgets.QWidget()
        self.stack4 = QtWidgets.QWidget()

        self.Window1UI()
        self.Window2UI()
        self.Window3UI()
        self.Window4UI()

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)

    def Window1UI(self):
        self.stack1.setFixedSize(480, 800)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)

        # PushButton1
        self.PushButton1 = QtWidgets.QPushButton(self.stack1)
        self.PushButton1.setText("Начать")
        self.PushButton1.setGeometry(QtCore.QRect(10, 700, 460, 30))

        # label1
        self.label1 = QtWidgets.QLabel(self.stack1)
        self.label1.setText("Добро пожаловать. Давайте начнём")
        self.label1.setGeometry(10, 10, 470, 50)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(font)

    def Window2UI(self):
        self.stack2.setFixedSize(480, 800)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)

        # PushButton2
        self.PushButton2 = QtWidgets.QPushButton(self.stack2)
        self.PushButton2.setGeometry(QtCore.QRect(10, 700, 460, 30))
        self.PushButton2.setText("Следующий вопрос")

        # radioButton1
        self.radioButton1 = QtWidgets.QRadioButton(self.stack2)
        self.radioButton1.setText("Ответ а")
        self.radioButton1.setChecked(False)
        self.radioButton1.answer = 1
        self.radioButton1.setGeometry(QtCore.QRect(10, 600, 460, 30))
        self.radioButton1.setFont(font)

        # radioButton2
        self.radioButton2 = QtWidgets.QRadioButton(self.stack2)
        self.radioButton2.setText("Ответ б")
        self.radioButton2.setChecked(False)
        self.radioButton2.answer = 0
        self.radioButton2.setGeometry(QtCore.QRect(10, 650, 460, 30))
        self.radioButton2.setFont(font)

    def Window3UI(self):

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)

        self.stack3.setFixedSize(480, 800)

        # PushButton3
        self.PushButton3 = QtWidgets.QPushButton(self.stack3)
        self.PushButton3.setText("Завершить тест")
        self.PushButton3.setGeometry(QtCore.QRect(10, 700, 460, 30))

        # radioButton3
        self.radioButton3 = QtWidgets.QRadioButton(self.stack3)
        self.radioButton3.setText("Ответ а")
        self.radioButton3.setChecked(False)
        self.radioButton3.answer = "correct"
        self.radioButton3.setGeometry(QtCore.QRect(10, 600, 460, 30))
        self.radioButton3.setFont(font)

        # radioButton4
        self.radioButton4 = QtWidgets.QRadioButton(self.stack3)
        self.radioButton4.setText("Ответ б")
        self.radioButton4.setChecked(False)
        self.radioButton4.answer = "false"
        self.radioButton4.setGeometry(QtCore.QRect(10, 650, 460, 30))
        self.radioButton4.setFont(font)



    def Window4UI(self):
        self.stack4.setFixedSize(480, 800)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)

        # label2
        self.label2 = QtWidgets.QLabel(self.stack4)
        self.label2.setText("Тест окончен. \nРезультаты теста:")
        self.label2.setGeometry(10, 40, 470, 100)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(font)

        #label3
        self.label3 = QtWidgets.QLabel(self.stack4)
        self.label3.setGeometry(10, 210, 470, 310)
        self.label3.setAlignment(Qt.AlignLeft)
        self.label3.setFont(font)

        # PushButton4
        self.PushButton4 = QtWidgets.QPushButton(self.stack4)
        self.PushButton4.setText("Вернуться к ответам")
        self.PushButton4.setGeometry(QtCore.QRect(10, 700, 460, 30))
