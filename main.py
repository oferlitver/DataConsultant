# -*- coding: utf-8 -*-

"""main file of experiment"""


import sys
from PyQt5.QtWidgets import (QWidget, QDialog, QApplication, QStackedWidget, 
                             QGroupBox, QVBoxLayout, QCheckBox, QPushButton,
                             QLabel, QFrame, QGridLayout)
from newUser import NewUserForm
from data_window import DataWidget

__author__ = 'Ofer Litver'
# TODO replace with value from config
NUM_STEPS = 3


class FlowDialog(QWidget):

    def __init__(self, parent=None):
        super(FlowDialog, self).__init__(parent)
        self._n_steps = 0  # number of performed steps

        self.pagesWidget = QStackedWidget()
        self.pagesWidget.addWidget(NewUserForm())
        self.pagesWidget.addWidget(DataWidget())
        self.nextButton = QPushButton("&Next")
        self.nextButton.pressed.connect(self.nextPressed)
        mainLayout = QGridLayout()
        # set screen shoulders
        mainLayout.setRowMinimumHeight(0, 80)
        mainLayout.setRowMinimumHeight(3, 80)
        mainLayout.setColumnMinimumWidth(0, 80)
        mainLayout.setColumnMinimumWidth(2, 80)
        mainLayout.addWidget(self.pagesWidget, 1, 1)
        mainLayout.addWidget(self.nextButton, 2, 1)
        self.setLayout(mainLayout)

    def nextPressed(self):
        """
        control the order and number of repetitions of the experiment
        :return:
        """
        if self.pagesWidget.currentIndex() == 0:  # if on new_user screen
            self._n_steps += 1
            self.pagesWidget.setCurrentIndex(1)
        elif self.pagesWidget.currentIndex() == 1:
            if self._n_steps < NUM_STEPS:
                self._n_steps += 1
                print("Step number {}".format(self._n_steps))
        elif self.pagesWidget.currentIndex() == 2:
            print("That's it")
        else:
            raise RuntimeError("No such index")


def main():
    app = QApplication(sys.argv)
    experiment = FlowDialog()
    experiment.showFullScreen()
    app.exec_()


if __name__ == "__main__":
    main()
