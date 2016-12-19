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


class DataWidget(QWidget):

    def __init__(self):
        super(DataWidget, self).__init__(None)
        self.read_data_file(HISTORIC_DATA)
        self.start_date = date(2016, 10, 1)
        self.end_date = date(2016, 11, 1)
        self.graph = GraphCanvas(self.data_frame)
        
        # options group box
        self.optionsGroupBox = QGroupBox("Options")
        options_layout = QVBoxLayout()
        dateRangeLayout = QFormLayout()
        startDateLabel = QLabel("Start Date:")
        self.start_date_box = QDateEdit(self.start_date)
        self.start_date_box.setCalendarPopup(True)
        self.start_date_box.setDisplayFormat(DATE_DISPLAY_FORMAT)
        self.start_date_box.dateChanged.connect(self.plot)
        end_date_label = QLabel("End Date:")
        self.end_date_box = QDateEdit(self.end_date)
        self.end_date_box.setCalendarPopup(True)
        self.end_date_box.setDisplayFormat(DATE_DISPLAY_FORMAT)
        self.end_date_box.dateChanged.connect(self.plot)
        dateRangeLayout.addRow(startDateLabel, self.start_date_box)
        dateRangeLayout.addRow(end_date_label, self.end_date_box)
        # days of week
        self.sundayCheckBox = QCheckBox("Sunday")
        self.mondayCheckBox = QCheckBox("Monday")
        self.tuesdayCheckBox = QCheckBox("Tuesday")
        self.wednesdayCheckBox = QCheckBox("Wednesday")
        self.thursdayCheckBox = QCheckBox("Thursday")
        self.fridayCheckBox = QCheckBox("Friday")
        self.saturdayCheckBox = QCheckBox("Saturday")
        self.sundayCheckBox.toggled.connect(self.plot)
        self.mondayCheckBox.toggled.connect(self.plot)
        self.tuesdayCheckBox.toggled.connect(self.plot)
        self.wednesdayCheckBox.toggled.connect(self.plot)
        self.thursdayCheckBox.toggled.connect(self.plot)
        self.fridayCheckBox.toggled.connect(self.plot)
        self.saturdayCheckBox.toggled.connect(self.plot)
        # 
        options_layout.addLayout(dateRangeLayout)
        options_layout.addWidget(self.sundayCheckBox)
        options_layout.addWidget(self.mondayCheckBox)
        options_layout.addWidget(self.tuesdayCheckBox)
        options_layout.addWidget(self.wednesdayCheckBox)
        options_layout.addWidget(self.thursdayCheckBox)
        options_layout.addWidget(self.fridayCheckBox)
        options_layout.addWidget(self.saturdayCheckBox)
        options_layout.addWidget(QPushButton("Button"))
        self.optionsGroupBox.setLayout(options_layout)
        
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
                                      #header=0,
                                      index_col=0,
                                      parse_dates=True)
                                      #date_parser=dateparse)

    def plot(self):
        """Method to update start / end dates upon selection. Fetch the start /
        end dates, convert the QTime datatype to DateTime.Date datatype, and
        plot the graph.
        """
        self.start_date = self.start_date_box.date().toPyDate()
        self.end_date = self.end_date_box.date().toPyDate()
        self.graph.plot(self.data_frame.loc[self.start_date : self.end_date])


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = DataWidget()
    window.show()
    app.exec_()
