# -*- coding: utf-8 -*-
__author__ = 'Ofer'

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DataWindow(QDialog):

    def __init__(self, parent=None):
        super(DataWindow, self).__init__(parent)
        self.createWidgets()
        self.layoutWidgets()
        self.createConnections()
        self.setWindowTitle("Main Window")

    def createWidgets(self):
        self.idLabel = QLabel("smthing")

    def layoutWidgets(self):
        grid = QGridLayout()
        grid.addWidget(self.idLabel, 0, 0)
        self.setLayout(grid)

    def createConnections(self):
        pass


def main():
    app = QApplication(sys.argv)
    form = DataWindow()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
