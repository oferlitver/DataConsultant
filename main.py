# -*- coding: utf-8 -*-

"""main file of experiment"""


import sys
import config
from PyQt5.QtWidgets import (QWidget, QDialog, QApplication, QStackedWidget, 
                             QGroupBox, QVBoxLayout, QCheckBox, QPushButton,
                             QLabel, QFrame, QGridLayout, QHBoxLayout)
from newUser import NewUserForm
from data_window import DataWidget

__author__ = 'Ofer Litver'


class FlowDialog(QWidget):

    def __init__(self, parent=None):
        super(FlowDialog, self).__init__(parent)
        self._n_steps = 1  # number of performed steps

        self.pages_widget = QStackedWidget()
        self.new_user_form = NewUserForm()
        self.data_widget = DataWidget()
        self.pages_widget.addWidget(self.new_user_form)
        self.pages_widget.addWidget(self.data_widget)
        self.next_button = QPushButton("&Next")
        self.next_button_layout = QHBoxLayout()
        self.next_button_layout.addStretch(1)
        self.next_button_layout.addWidget(self.next_button)
        self.next_button.pressed.connect(self.nextPressed)
        main_layout = QGridLayout()

        # set screen shoulders
        main_layout.setRowMinimumHeight(0, 80)
        main_layout.setRowMinimumHeight(3, 80)
        main_layout.setColumnMinimumWidth(0, 80)
        main_layout.setColumnMinimumWidth(2, 80)
        main_layout.addWidget(self.pages_widget, 1, 1)
        main_layout.addLayout(self.next_button_layout, 2, 1)
        self.setLayout(main_layout)

    def nextPressed(self):
        """
        control the order and number of repetitions of the experiment
        """
        self.data_widget.count_down_timer.restart_timer()  # restart timer
        if self.pages_widget.currentIndex() == 0:  # if on new_user screen
            self.new_user_form.save_results()
            self.pages_widget.setCurrentIndex(1)
        elif self.pages_widget.currentIndex() == 1:  # if on data screen
            if self._n_steps < config.NUM_STEPS:
                self.data_widget.add_log_row()
                self._n_steps += 1
                print("Step number {}".format(self._n_steps))  # DEBUGGING
        elif self.pages_widget.currentIndex() == 2:
            print("That's it")  # DEBUGGING
        else:
            # If reached wrong index
            raise RuntimeError("No such index")


def main():
    app = QApplication(sys.argv)
    experiment = FlowDialog()
    experiment.showFullScreen()
    app.exec_()


if __name__ == "__main__":
    main()
