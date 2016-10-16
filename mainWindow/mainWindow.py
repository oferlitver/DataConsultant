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
        
        self.createMenu()
        self.createOptionsGroupBox()
        self.createGraphGroupBox()
        self.createChoiceGroupBox()
        #self.createWidgets()
        #self.layoutWidgets()
        #self.createConnections()
        
        # left part of the screen - options & graph groupbox
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.optionsGroupBox)
        leftLayout.addWidget(self.graphGroupBox)
        
        mainLayout = QHBoxLayout()
        #mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.choiceGroupBox)
#        mainLayout.addWidget(self.
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Main Window")
        self.setMinimumSize(360, 240)

    def testPopup(self):
        test = QDialog()
        testLayout = QHBoxLayout()
        testLayout.addWidget(QLabel("test"))
        test.setLayout(testLayout)
        test.show()

    def createMenu(self):
        """self.menuBar = QMenuBar()
        
        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)
        
        self.exitAction.triggered.connect(sys.exit)
        """
        menu = self.menuBar().addMenu("&File")
        self.exitAction = QAction("E&xit", self)
        self.testAction = QAction("&Test", self)
        
        self.exitAction.triggered.connect(sys.exit)
        self.testAction.triggered.connect(self.testPopup)
        
        menu.addAction(self.exitAction)
        menu.addSeparator()
        menu.addAction(self.testAction)

    def createOptionsGroupBox(self):
        self.optionsGroupBox = QGroupBox("Options")
        layout = QVBoxLayout()
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

    def createWidgets(self):
        self.idLabel = QLabel("smthing")

    def layoutWidgets(self):
        grid = QGridLayout()
        grid.addWidget(self.idLabel, 0, 0)
        self.setLayout(grid)

    def createConnections(self):
        pass


def main():

    # import sys  # can i move it here for optimization???

    app = QApplication(sys.argv)
    window = DataWindow()
    window.show()
    #app.exec_()  # changed after menus.py example
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
