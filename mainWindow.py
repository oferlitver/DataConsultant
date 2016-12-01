# -*- coding: utf-8 -*-
__author__ = 'Ofer'

# TODO optimize before finilazing
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class DataWindow(QWidget):

    def __init__(self):
        super(DataWindow, self).__init__(None)
        
        self.createOptionsGroupBox()
        self.createGraphGroupBox()
        self.createChoiceGroupBox()
        self.createCentralWidget()
        self.setLayout(self.grid)
        
    def createOptionsGroupBox(self):
        self.optionsGroupBox = QGroupBox("Options")
        layout = QVBoxLayout()
        
        self.sundayCheckBox = QCheckBox("Sunday")
        self.mondayCheckBox = QCheckBox("Monday")
        self.tuesdayCheckBox = QCheckBox("Tuesday")
        
        layout.addWidget(self.sundayCheckBox)
        layout.addWidget(self.mondayCheckBox)
        layout.addWidget(self.tuesdayCheckBox)
        layout.addWidget(QPushButton("Button"))
        self.optionsGroupBox.setLayout(layout)
        
    def createGraphGroupBox(self):
        self.graphGroupBox = QGroupBox("Graph")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Graph"))
        self.graphGroupBox.setLayout(layout)
        
    def createChoiceGroupBox(self):
        self.choiceGroupBox = QGroupBox("Choice")
        layout = QVBoxLayout()
        layout.addWidget(QTextEdit())
        self.choiceGroupBox.setLayout(layout)

    def createCentralWidget(self):
    
        frame = QFrame(self)
        self.grid = QGridLayout(frame)
        self.grid.setSpacing(8)
        self.grid.setContentsMargins(4, 4, 4, 4)
        
        self.grid.addWidget(self.optionsGroupBox, 0, 0)
        self.grid.addWidget(self.graphGroupBox, 1, 0)
        self.grid.addWidget(self.choiceGroupBox, 0, 1)

def main():

    # import sys  # can i move it here for optimization???

    app = QApplication(sys.argv)
    window = DataWindow()
    window.showFullScreen()
    #~ app.setStyle(QStyleFactory.create("plastique"))
    #~ app.setStyle(QStyleFactory.create("cde"))
    #~ app.setStyle(QStyleFactory.create("motif"))
    #~ app.setStyle(QStyleFactory.create("sgi"))
    #~ app.setStyle(QStyleFactory.create("windows"))
    #~ app.setStyle(QStyleFactory.create("cleanlooks"))
    #~ app.setStyle(QStyleFactory.create("mac"))
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
