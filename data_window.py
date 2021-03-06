#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:15:16 2016

@author: ofer
"""
from datetime import date, datetime
import csv
import pandas as pd
from PyQt5.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QCheckBox,
    QPushButton, QLabel, QFrame, QGridLayout, QDateEdit, QFormLayout, QSpinBox,
    QLCDNumber, QHBoxLayout)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
import config
from graph import GraphCanvas


__author__ = 'Ofer Litver'


class DataWidget(QWidget):

    def __init__(self):
        super(DataWidget, self).__init__(None)
        self.read_data_file(config.HISTORIC_DATA)
        self.start_date = date(2016, 10, 1)
        self.end_date = date(2016, 11, 1)
        self.graph = GraphCanvas(self.data_frame)
        with open(config.LOGFILE, 'w', newline='') as logfile:
            logwriter = csv.writer(logfile)
            logwriter.writerow(config.headers)

        # options group box
        self.optionsGroupBox = QGroupBox("Options")
        options_layout = QVBoxLayout()
        date_range_layout = QFormLayout()
        start_date_label = QLabel("Start Date:")
        self.start_date_box = QDateEdit(self.start_date)
        self.start_date_box.setCalendarPopup(True)
        self.start_date_box.setDisplayFormat(config.DATE_DISPLAY_FORMAT)
        self.start_date_box.dateChanged.connect(self.plot)
        end_date_label = QLabel("End Date:")
        self.end_date_box = QDateEdit(self.end_date)
        self.end_date_box.setCalendarPopup(True)
        self.end_date_box.setDisplayFormat(config.DATE_DISPLAY_FORMAT)
        self.end_date_box.dateChanged.connect(self.plot)
        date_range_layout.addRow(start_date_label, self.start_date_box)
        date_range_layout.addRow(end_date_label, self.end_date_box)
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

        options_layout.addLayout(date_range_layout)
        options_layout.addWidget(self.sundayCheckBox)
        options_layout.addWidget(self.mondayCheckBox)
        options_layout.addWidget(self.tuesdayCheckBox)
        options_layout.addWidget(self.wednesdayCheckBox)
        options_layout.addWidget(self.thursdayCheckBox)
        options_layout.addWidget(self.fridayCheckBox)
        options_layout.addWidget(self.saturdayCheckBox)
        options_layout.addWidget(QPushButton("Button"))
        self.optionsGroupBox.setLayout(options_layout)

        # graph group box
        self.graphGroupBox = QGroupBox("Graph")
        graphLayout = QVBoxLayout()
        graphLayout.addWidget(self.graph)
        self.graphGroupBox.setLayout(graphLayout)

        # choice group box
        self.choiceGroupBox = QGroupBox("Choice")

        choice_layout = QVBoxLayout()

        choice_layout_1 = QHBoxLayout()
        choice_layout_1.addWidget(QLabel("A"))
        choice_layout_1.addWidget(QLabel("B"))
        choice_layout_1.addWidget(QLabel("C"))
        choice_layout_1.addWidget(QLabel("D"))

        choice_layout_2 = QHBoxLayout()
        self.decision_value_1 = QSpinBox()
        self.decision_value_2 = QSpinBox()
        self.decision_value_3 = QSpinBox()
        self.decision_value_4 = QSpinBox()
        choice_layout_2.addWidget(self.decision_value_1)
        choice_layout_2.addWidget(self.decision_value_2)
        choice_layout_2.addWidget(self.decision_value_3)
        choice_layout_2.addWidget(self.decision_value_4)

        choice_layout.addLayout(choice_layout_1)
        choice_layout.addLayout(choice_layout_2)

        self.decision_value_1.setValue(42)

        self.choiceGroupBox.setLayout(choice_layout)

        # count-down timer
        self.timerGroupBox = QGroupBox("Timer")
        timer_layout = QVBoxLayout()
        self.timerGroupBox.setLayout(timer_layout)
        self.count_down_timer = CountDownTimer()
        timer_layout.addWidget(self.count_down_timer.lcd)

        # central widget
        frame = QFrame(self)
        self.grid = QGridLayout(frame)
        self.grid.setSpacing(16)
        self.grid.setContentsMargins(16, 16, 16, 16)
        self.grid.addWidget(self.optionsGroupBox, 0, 0, 2, 1)
        self.grid.addWidget(self.graphGroupBox, 0, 1, 2, 1)
        self.grid.addWidget(self.timerGroupBox, 0, 2)
        self.grid.addWidget(self.choiceGroupBox, 2, 1)
        self.grid.setColumnStretch(0, 2)
        self.grid.setColumnStretch(1, 6)
        self.grid.setColumnStretch(2, 1)
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 2)
        self.grid.setRowStretch(2, 2)
        self.setLayout(self.grid)

    def read_data_file(self, data_file):
        """read data_file and import it's content as pandas dataframe"""
        dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
        self.data_frame = pd.read_csv(data_file,
                                      index_col=0,
                                      parse_dates=True)

    def plot(self):
        """
        Method to update start / end dates upon selection. Fetch the start /
        end dates, convert the QTime datatype to DateTime.Date datatype, and
        plot the graph.
        """
        self.start_date = self.start_date_box.date().toPyDate()
        self.end_date = self.end_date_box.date().toPyDate()
        self.graph.plot(self.data_frame.loc[self.start_date : self.end_date])

    def add_log_row(self):
        """
        Write data in the log file
        :return:
        """
        new_row = [config.id, config.age, config.male, config.field,
                   'test_condition', datetime.now()]
        with open(config.LOGFILE, 'a', newline='') as logfile:
            logwriter = csv.writer(logfile)
            logwriter.writerow(new_row)


class CountDownTimer(QLCDNumber):
    """
    time_allocation: positive integer, indicating the allocated time for user
    time_value: started as time_allocation, and dynamically changed every second
    """

    def __init__(self, time_allocation=15, parent=None):
        super(CountDownTimer, self).__init__(parent)
        self.time_allocation = time_allocation
        self.time_value = self.time_allocation

        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.advance_time)

        # LCD time display
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(3)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(self.time_value)

    def restart_timer(self):
        self.time_value = self.time_allocation
        self.lcd.display(self.time_value)
        palette = self.lcd.palette()
        palette.setColor(palette.WindowText, QColor(0, 0, 0))
        self.lcd.setPalette(palette)
        self.timer.start(1000)

    def advance_time(self):
        self.time_value -= 1

        # Yellow - five seconds left
        if self.time_value == 5:
            palette = self.lcd.palette()
            palette.setColor(palette.WindowText, QColor(255, 153, 0))
            self.lcd.setPalette(palette)

        # Red - no time left
        if self.time_value == 0:
            palette = self.lcd.palette()
            palette.setColor(palette.WindowText, QColor(255, 0, 0))
            self.lcd.setPalette(palette)
        self.lcd.display(self.time_value)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = DataWidget()
    window.show()
    app.exec_()
