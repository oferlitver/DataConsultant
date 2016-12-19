#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:04:56 2016

@author: ofer
"""

import sys
import numpy as np
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QApplication)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphCanvas(FigureCanvas):

    def __init__(self, data_frame, parent=None):
        """data_frame is Pandas DataFrame"""
        if data_frame is None:
            self.generate_data()
        else:
            self.data = data_frame
        self.fig = Figure()
        # TODO change to dynamic ylim
        self.axes = self.fig.add_subplot(111, ylim=(0.0, 200.0))
        self.axes.hold(False)
        FigureCanvas.__init__(self, self.fig)
        self.plot(data_frame)

    def plot(self, data_frame):
        """takes a Pandas DataFrame and plots it"""
        self.axes.plot(data_frame, 'o-')
        self.axes.set_ylim(0.0, 200.0)
        self.fig.autofmt_xdate()
        self.draw()

    def generate_data(self):
        """for debugging purposes"""
        self.data = np.random.randint(1, 10, 10)


class ApplicationWindow(QWidget):
    """for debugging porposes only"""
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