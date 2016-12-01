#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:15:16 2016

@author: ofer
"""
from PyQt5.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QCheckBox,
                             QPushButton, QLabel, QFrame, QGridLayout)
from graph_window import GraphCanvas


class DataWindow(QWidget):

    def __init__(self):
        super(DataWindow, self).__init__(None)
        self.graph = GraphCanvas()

        self.createOptionsGroupBox()
        self.createGraphGroupBox()
        self.createChoiceGroupBox()
        self.createCentralWidget()
        self.setLayout(self.grid)

    def createChoiceGroupBox(self):
        self.choiceGroupBox = QGroupBox("Choice")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("placeholder"))
        self.choiceGroupBox.setLayout(layout)

    def createOptionsGroupBox(self):
        self.optionsGroupBox = QGroupBox("Options")
        layout = QVBoxLayout()

        self.sundayCheckBox = QCheckBox("Sunday")
        self.mondayCheckBox = QCheckBox("Monday")
        self.tuesdayCheckBox = QCheckBox("Tuesday")
        self.wednesdayCheckBox = QCheckBox("Wednesday")
        self.thursdayCheckBox = QCheckBox("Thursday")
        self.fridayCheckBox = QCheckBox("Friday")
        self.saturdayCheckBox = QCheckBox("Saturday")

        self.sundayCheckBox.toggled.connect(self.graph.plot)

        layout.addWidget(self.sundayCheckBox)
        layout.addWidget(self.mondayCheckBox)
        layout.addWidget(self.tuesdayCheckBox)
        layout.addWidget(self.wednesdayCheckBox)
        layout.addWidget(self.thursdayCheckBox)
        layout.addWidget(self.fridayCheckBox)
        layout.addWidget(self.saturdayCheckBox)
        layout.addWidget(QPushButton("Button"))
        self.optionsGroupBox.setLayout(layout)

    def createGraphGroupBox(self):
        self.graphGroupBox = QGroupBox("Graph")
        layout = QVBoxLayout()
        layout.addWidget(self.graph)
        self.graphGroupBox.setLayout(layout)

    def createCentralWidget(self):
        frame = QFrame(self)
        self.grid = QGridLayout(frame)
        self.grid.setSpacing(8)
        self.grid.setContentsMargins(4, 4, 4, 4)

        self.grid.addWidget(self.optionsGroupBox, 0, 0)
        self.grid.addWidget(self.graphGroupBox, 0, 1)
        self.grid.addWidget(self.choiceGroupBox, 1, 0)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = DataWindow()
    window.show()
    app.exec_()