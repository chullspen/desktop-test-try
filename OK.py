from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QToolTip, QPushButton, QApplication, QWidget, QLabel)
import sys

from Okay import Ui_Okay

class OK(QMainWindow, Ui_Okay):
    def __init__(self, parent=None):
        super(OK, self).__init__(parent)
        self.setupUi(self)

        self.PushButton1.clicked.connect(self.OpenWindow1)
        self.PushButton2.clicked.connect(self.OpenWindow2)
        self.PushButton3.clicked.connect(self.OpenWindow3)
        self.PushButton4.clicked.connect(self.OpenWindow1)

        self.radioButton1.toggled.connect(self.finalScore)
        self.radioButton2.toggled.connect(self.finalScore)

        self.radioButton3.toggled.connect(self.finalScore)
        self.radioButton4.toggled.connect(self.finalScore)

    def OpenWindow1(self):
        self.QtStack.setCurrentIndex(1)

    def OpenWindow2(self):
        self.QtStack.setCurrentIndex(2)

    def OpenWindow3(self):
        self.QtStack.setCurrentIndex(3)

    def finalScore(self):
        # Question1
        score_q1 = 0
        if self.radioButton1.isChecked():
            score_q1 += 0
        else:
            score_q1 += 0

        if self.radioButton2.isChecked():
            score_q1 += 1
        else:
            score_q1 += 0

        if self.radioButton1.isChecked() and self.radioButton2.isChecked() == False:
            score_q1 += 0

        # Question2
        score_q2 = 0
        if self.radioButton3.isChecked():
            score_q2 += 1
        else:
            score_q2 += 0

        if self.radioButton4.isChecked():
            score_q2 += 0
        else:
            score_q2 += 0

        if self.radioButton3.isChecked() and self.radioButton4.isChecked() == False:
            score_q2 += 0

        final_score = score_q1 + score_q2
        if final_score == 0:
            self.label3.setText("У вас нет правильных ответов. \nУдачи в следующий раз.")
        elif final_score == 1:
            self.label3.setText("У вас " + str(final_score) + " правильный ответ из 2.")
        else:
            self.label3.setText("У вас " + str(final_score) + " правильных ответов из 2.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = OK()
    sys.exit(app.exec_())
