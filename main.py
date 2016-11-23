# -*- coding: utf-8 -*-

"""main file of experiment"""


import sys

from numpy import pi, sin, arange

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


__author__ = 'Ofer Litver'



class NewUserForm(QWidget):

    def __init__(self, parent=None):
        super(NewUserForm, self).__init__(parent)
        self.createWidgets()
        self.layoutWidgets()
        self.createConnections()

        nextwin = DataWindow()
        self.setLayout(nextwin.grid)

    def createWidgets(self):
        self.title = QLabel("Welcome!")
        titleFont = QFont()
        titleFont.setPointSize(36)
        titleFont.setItalic(True)
        self.title.setFont(titleFont)
        self.subtitle = QLabel("Before we begin the experiment, please fill the following details. Those details will be kept completely confidential and used for the sole purpose of the experiment.")
        self.subtitle.setWordWrap(True)

        self.idLabel = QLabel("&Identification number")
        self.idLineEdit = QLineEdit()
        # TODO add validation
        regexp = QRegExp('^\d{8,9}$')
        validator = QRegExpValidator(regexp)
        self.idLineEdit.setValidator(validator)
        self.idLabel.setBuddy(self.idLineEdit)

        self.ageLabel = QLabel("&Age:")
        self.ageSpinBox = QSpinBox()
        self.ageSpinBox.setRange(16, 80)
        self.ageSpinBox.setValue(20)
        self.ageLabel.setBuddy(self.ageSpinBox)

        self.genderLabel = QLabel("&Gender:")
        self.maleRadioButton = QRadioButton("Male")
        self.femaleRadioButton = QRadioButton("Female")
        self.genderButtonGroup = QButtonGroup()
        self.genderButtonGroup.addButton(self.maleRadioButton, 1)
        self.genderButtonGroup.addButton(self.femaleRadioButton, 2)
        self.genderLayout = QHBoxLayout()
        self.genderLayout.addWidget(self.maleRadioButton)
        self.genderLayout.addWidget(self.femaleRadioButton)
        self.genderLabel.setBuddy(self.maleRadioButton)

        self.fieldLabel = QLabel("Primary &field of studies:")
        field_list = ["--- Please select ---",
                      "Electrical Engineering",
                      "Mechanical Engineering",
                      "Industrial Engineering",
                      "Biomedical Engineering",
                      "Environmental Engineering"]
        self.fieldComboBox = QComboBox()
        self.fieldComboBox.addItems(field_list)
        self.fieldLabel.setBuddy(self.fieldComboBox)

        self.nextButton = QPushButton("Next >")
        self.buttonBox = QDialogButtonBox(self.nextButton)

    def layoutWidgets(self):
        screenLayout = QGridLayout()
        screenLayout.setSpacing(20)
        screenLayout.setColumnStretch(0, 2)
        screenLayout.setColumnStretch(3, 1)
        screenLayout.setColumnStretch(4, 1)
        screenLayout.setRowStretch(0, 1)
        
        screenLayout.addWidget(self.title, 1, 1, 1, 2)
        screenLayout.setRowMinimumHeight(2, 50)
        screenLayout.addWidget(self.subtitle, 3, 1, 1, 2)
        screenLayout.addWidget(self.idLabel, 4, 1)
        screenLayout.addWidget(self.idLineEdit, 4, 2)
        screenLayout.addWidget(self.ageLabel, 5, 1)
        screenLayout.addWidget(self.ageSpinBox, 5, 2)
        screenLayout.addWidget(self.genderLabel, 6, 1)
        screenLayout.addLayout(self.genderLayout, 6, 2)
        screenLayout.addWidget(self.fieldLabel, 7, 1)
        screenLayout.addWidget(self.fieldComboBox, 7, 2)
        screenLayout.setRowMinimumHeight(8, 30)
        screenLayout.addWidget(self.nextButton, 9, 2)
        screenLayout.setRowStretch(10, 1)

        self.setLayout(screenLayout)

    def createConnections(self):
        self.nextButton.clicked.connect(self.accepted)

    def accepted(self):
        self.writeResults()

    def writeResults(self):
        # get value of gender checkbox and convert
        # 1 --> m
        # 2 --> f
        g = self.genderButtonGroup.checkedId()
        gender = 'm' if g == 1 else 'f' if g == 2 else '-'

        # write results to CSV file
        file = open("output/data.csv", "w")
        file.write(self.idLineEdit.text() + ',' +
                   str(self.ageSpinBox.value()) + ',' +
                   gender + ',' +
                   self.fieldComboBox.currentText())
        file.close()

    def rejected(self):
        # in case of pressing "Cancel"
        self.closeEvent(self)

    def closeEvent(self, event):
        # in case of clicking on X
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class GraphCanvas(FigureCanvas):

    def __init__(self, x=None, y=None, parent=None, width=5, height=4, dpi=100):
        self.x = x
        self.y = y
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # clear the axes every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.t = arange(0.0, 3.0, 0.01)
        self.s = sin(2*pi*self.t)
        self.axes.plot(self.t, self.s)

    def update_figure(self):
        self.s += 0.1
        self.axes.plot(self.t, self.s)
        self.draw()


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
        layout.addWidget(self.graph)
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

        self.sundayCheckBox.toggled.connect(self.graph.update_figure)

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
        layout.addWidget(QPushButton("Graph"))
        self.graphGroupBox.setLayout(layout)

    def createCentralWidget(self):

        frame = QFrame(self)
        self.grid = QGridLayout(frame)
        self.grid.setSpacing(8)
        self.grid.setContentsMargins(4, 4, 4, 4)

        self.grid.addWidget(self.optionsGroupBox, 0, 0)
        self.grid.addWidget(self.graphGroupBox, 1, 0)
        self.grid.addWidget(self.choiceGroupBox, 0, 1)


class FlowDialog(QDialog):
    def __init__(self, parent=None):
        super(FlowDialog, self).__init__(parent)

        self.pagesWidget = QStackedWidget()
        self.pagesWidget.addWidget(NewUserForm())
        self.pagesWidget.addWidget(DataWindow())

        self.nextButton = QPushButton("Next")
        self.nextButton.pressed.connect(self.nextPressed)

        mainLayout = QGridLayout()

        # set screen shoulders
        mainLayout.setRowMinimumHeight(0, 80)
        mainLayout.setRowMinimumHeight(3, 20)
        mainLayout.setColumnMinimumWidth(0, 20)
        mainLayout.setColumnMinimumWidth(2, 20)

        mainLayout.addWidget(self.pagesWidget, 1, 1)
        mainLayout.addWidget(self.nextButton, 2, 1)
        self.setLayout(mainLayout)

    def nextPressed(self):
        self.pagesWidget.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    experiment = FlowDialog()
    experiment.showFullScreen()
    app.exec_()

if __name__ == "__main__":
    main()
