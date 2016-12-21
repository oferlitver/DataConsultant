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

        self.pages_widget = QStackedWidget()
        self.pages_widget.addWidget(NewUserForm())
        self.pages_widget.addWidget(DataWidget())
        self.next_button = QPushButton("&Next")
        self.next_button.pressed.connect(self.nextPressed)
        main_layout = QGridLayout()
        # set screen shoulders
        main_layout.setRowMinimumHeight(0, 80)
        main_layout.setRowMinimumHeight(3, 80)
        main_layout.setColumnMinimumWidth(0, 80)
        main_layout.setColumnMinimumWidth(2, 80)
        main_layout.addWidget(self.pages_widget, 1, 1)
        main_layout.addWidget(self.next_button, 2, 1)
        self.setLayout(main_layout)

    def nextPressed(self):
        """
        control the order and number of repetitions of the experiment
        :return:
        """
        if self.pages_widget.currentIndex() == 0:  # if on new_user screen
            self._n_steps += 1
            self.pages_widget.setCurrentIndex(1)
        elif self.pages_widget.currentIndex() == 1:
            if self._n_steps < NUM_STEPS:
                self._n_steps += 1
                print("Step number {}".format(self._n_steps))
        elif self.pages_widget.currentIndex() == 2:
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
