# -*- coding: utf-8 -*-
__author__ = 'Ofer'

# TODO optimize before finilazing
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class DataWindow(QMainWindow):

    def __init__(self):
        super(DataWindow, self).__init__(None)
        
        self.createActions()
        self.createMenus()
        self.createOptionsGroupBox()
        self.createGraphGroupBox()
        self.createChoiceGroupBox()
        
        self.centralWidget = self.createCentralWidget()
        self.setCentralWidget(self.centralWidget)
        
        # left part of the screen - options & graph groupbox
        #leftLayout = QVBoxLayout()
        #leftLayout.addWidget(self.optionsGroupBox)
        #leftLayout.addWidget(self.graphGroupBox)
        
        #mainLayout = QHBoxLayout()
        #mainLayout.setMenuBar(self.menuBar)
        #mainLayout.addWidget(self.choiceGroupBox)
        #mainLayout.addWidget(self.testLabel)
        #mainLayout.addWidget(self.
        #self.setLayout(mainLayout)
        
        self.setMinimumSize(150, 100)
        self.setWindowTitle("Main Window")

    def new(self):
        self.testLabel.setText("test succeded")

    def createActions(self):
        self.newAction = QAction("&New", self, triggered=self.new)

    def createMenus(self):
        """self.menuBar = QMenuBar()
        
        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)
        
        self.exitAction.triggered.connect(sys.exit)
        """
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        #self.fileMenu.addAction(self.exitAction)

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
        grid = QGridLayout(frame)
        grid.setSpacing(8)
        grid.setContentsMargins(4, 4, 4, 4)
        
        grid.addWidget(self.optionsGroupBox, 0, 0)
        grid.addWidget(self.graphGroupBox, 1, 0)
        grid.addWidget(self.choiceGroupBox, 0, 1)
        
        return frame

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
