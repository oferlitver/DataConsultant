#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:04:56 2016

@author: ofer
"""

import sys

import numpy as np

#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QApplication)

#import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphCanvas(FigureCanvas):

    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)

        FigureCanvas.__init__(self, fig)

#        QWidget.__init__(self, parent)
#        self.figure = plt.figure()
#        self.figure_canvas = FigureCanvas(self.figure)
#        # self.canvas = FigureCanvas(self.figure)

    def plot(self):
        data = np.random.randint(1, 10, 10)
        #ax = self.figure.add_subplot(111)
        #ax.hold(True)
        #ax.plot(data, '*-')
        self.axes.plot(data)
        self.draw()


class ApplicationWindow(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        
        self.graph = GraphCanvas()
        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.graph.plot)
        
        layout = QVBoxLayout()
        layout.addWidget(self.graph)
        layout.addWidget(self.button)
        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    graph = ApplicationWindow()
    graph.show()
    sys.exit(app.exec_())