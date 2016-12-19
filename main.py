# -*- coding: utf-8 -*-

"""main file of experiment"""


import sys
from PyQt5.QtWidgets import (QWidget, QDialog, QApplication, QStackedWidget, 
                             QGroupBox, QVBoxLayout, QCheckBox, QPushButton,
                             QLabel, QFrame, QGridLayout)
from newUser import NewUserForm
from data_window import DataWidget

__author__ = 'Ofer Litver'


class FlowDialog(QWidget):

    def __init__(self, parent=None):
        super(FlowDialog, self).__init__(parent)
        self.pagesWidget = QStackedWidget()
        self.pagesWidget.addWidget(NewUserForm())
        self.pagesWidget.addWidget(DataWidget())
        self.nextButton = QPushButton("Next")
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
        self.pagesWidget.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    experiment = FlowDialog()
    experiment.showFullScreen()
    app.exec_()


if __name__ == "__main__":
    main()
