#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:15:16 2016

@author: ofer
"""
from datetime import date

import pandas as pd
from PyQt5.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QCheckBox,
                             QPushButton, QLabel, QFrame, QGridLayout,
                             QDateEdit, QFormLayout)

from graph import GraphCanvas

DATE_DISPLAY_FORMAT = "dd/MM/yyyy"
HISTORIC_DATA = "./data/historic_data.csv"
# HISTORIC_DATA = "./data/sample_data.csv"


class DataWidget(QWidget):

    def __init__(self):
        super(DataWidget, self).__init__(None)
        self.read_data_file(HISTORIC_DATA)
        self.start_date = date(2016, 10, 1)
        self.end_date = date(2016, 12, 1)
        self.graph = GraphCanvas(self.data_frame)
        
        # options group box
        self.optionsGroupBox = QGroupBox("Options")
        optionsLayout = QVBoxLayout()
        dateRangeLayout = QFormLayout()
        startDateLabel = QLabel("Start Date:")
        self.startDateBox = QDateEdit(self.start_date)
        self.startDateBox.setCalendarPopup(True)
        self.startDateBox.setDisplayFormat(DATE_DISPLAY_FORMAT)
        self.startDateBox.dateChanged.connect(self.graph.plot)
        endDateLabel = QLabel("End Date:")
        self.endDateBox = QDateEdit(self.end_date)
        self.endDateBox.setCalendarPopup(True)
        self.endDateBox.setDisplayFormat(DATE_DISPLAY_FORMAT)
        self.endDateBox.dateChanged.connect(self.graph.plot)
        dateRangeLayout.addRow(startDateLabel, self.startDateBox)
        dateRangeLayout.addRow(endDateLabel, self.endDateBox)
        # days of week
        self.sundayCheckBox = QCheckBox("Sunday")
        self.mondayCheckBox = QCheckBox("Monday")
        self.tuesdayCheckBox = QCheckBox("Tuesday")
        self.wednesdayCheckBox = QCheckBox("Wednesday")
        self.thursdayCheckBox = QCheckBox("Thursday")
        self.fridayCheckBox = QCheckBox("Friday")
        self.saturdayCheckBox = QCheckBox("Saturday")
        self.sundayCheckBox.toggled.connect(self.graph.plot)
        self.mondayCheckBox.toggled.connect(self.graph.plot)
        self.tuesdayCheckBox.toggled.connect(self.graph.plot)
        self.wednesdayCheckBox.toggled.connect(self.graph.plot)
        self.thursdayCheckBox.toggled.connect(self.graph.plot)
        self.fridayCheckBox.toggled.connect(self.graph.plot)
        self.saturdayCheckBox.toggled.connect(self.graph.plot)
        # 
        optionsLayout.addLayout(dateRangeLayout)
        optionsLayout.addWidget(self.sundayCheckBox)
        optionsLayout.addWidget(self.mondayCheckBox)
        optionsLayout.addWidget(self.tuesdayCheckBox)
        optionsLayout.addWidget(self.wednesdayCheckBox)
        optionsLayout.addWidget(self.thursdayCheckBox)
        optionsLayout.addWidget(self.fridayCheckBox)
        optionsLayout.addWidget(self.saturdayCheckBox)
        optionsLayout.addWidget(QPushButton("Button"))
        self.optionsGroupBox.setLayout(optionsLayout)
        
        # choice group box
        self.choiceGroupBox = QGroupBox("Choice")
        choiceLayout = QVBoxLayout()
        choiceLayout.addWidget(QLabel("placeholder"))
        self.choiceGroupBox.setLayout(choiceLayout)
        
        # graph group box
        self.graphGroupBox = QGroupBox("Graph")

        graphLayout = QVBoxLayout()
        graphLayout.addWidget(self.graph)
        self.graphGroupBox.setLayout(graphLayout)

        # central widget
        frame = QFrame(self)
        self.grid = QGridLayout(frame)
        self.grid.setSpacing(16)
        self.grid.setContentsMargins(16, 16, 16, 16)
        self.grid.addWidget(self.optionsGroupBox, 0, 0)
        self.grid.addWidget(self.graphGroupBox, 0, 1)
        self.grid.addWidget(self.choiceGroupBox, 1, 0)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 3)
        self.grid.setRowStretch(0, 2)
        self.grid.setRowStretch(1, 1)
        self.setLayout(self.grid)

    def read_data_file(self, data_file):
        """read data_file and import it's content as pandas dataframe"""
        dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
        self.data_frame = pd.read_csv(data_file,
                                      header=0,
                                      index_col=0,
                                      parse_dates=True,
                                      date_parser=dateparse)

    def update_date(self, date_type):
        """method to update start / end dates upon selection"""
        pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = DataWidget()
    window.show()
    app.exec_()