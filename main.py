# -*- coding: utf-8 -*-

"""main file of experiment"""


import sys
import config
from PyQt5.QtWidgets import (QWidget, QDialog, QApplication, QStackedWidget, 
                             QGroupBox, QVBoxLayout, QCheckBox, QPushButton,
                             QLabel, QFrame, QGridLayout, QHBoxLayout)
from newUser import NewUserForm, ExperimentSetup
from data_window import DataWidget
from instructions import InstructionsScreen


__author__ = 'Ofer Litver'
__email__ = 'oferlitver@gmail.com'


class FlowDialog(QWidget):
    """
    Class for controlling the order of screens in the experiment.
    """

    def __init__(self, parent=None):
        super(FlowDialog, self).__init__(parent)
        self._n_steps = 1  # number of performed steps

        self.pages_widget = QStackedWidget()

        # create widgets
        self.experiment_setup = ExperimentSetup()
        self.instructions = InstructionsScreen("./instructions/he-informed-consent.txt")
        self.new_user_form = NewUserForm()
        self.data_widget = DataWidget()

        # add widgets to pages_widget
        self.pages_widget.addWidget(self.experiment_setup)
        self.pages_widget.addWidget(self.instructions)
        self.pages_widget.addWidget(self.new_user_form)
        self.pages_widget.addWidget(self.data_widget)

        # next button
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
        self.pages_widget.setCurrentIndex(0)

    def nextPressed(self):
        """
        control the order and number of repetitions of the experiment
        """
        self.data_widget.count_down_timer.restart_timer()  # restart timer

        # if on setup screen
        if self.pages_widget.currentIndex() == 0:
            # get condition index number
            condition_index = self.experiment_setup.conditions_combo.currentIndex()
            # DEBUGGING:
            debug_condition = config.CONDITIONS['a'][condition_index]
            print(debug_condition)

            self.raise_index()

        # welcome screen
        elif self.pages_widget.currentIndex() == 1:
            self.raise_index()

        # if on new_user screen
        elif self.pages_widget.currentIndex() == 2:
            self.new_user_form.save_results()
            self.raise_index()

        # if on data screen
        elif self.pages_widget.currentIndex() == 3:
            if self._n_steps < config.NUM_STEPS:
                self.data_widget.add_log_row()
                self._n_steps += 1
                print("Step number {}".format(self._n_steps))  # DEBUGGING
            else:
                self.raise_index()

        elif self.pages_widget.currentIndex() == 4:
            print("That's it")  # DEBUGGING

        else:
            # If reached wrong index
            raise RuntimeError("No such index")

    def raise_index(self):
        current = self.pages_widget.currentIndex()
        self.pages_widget.setCurrentIndex(current + 1)


def main():
    app = QApplication(sys.argv)
    experiment = FlowDialog()
    experiment.showFullScreen()
    app.exec_()


if __name__ == "__main__":
    main()
