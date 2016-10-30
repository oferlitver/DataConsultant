#-*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# TODO finish this
#from DataConsultant.styles import styles


__author__ = 'Ofer Litver'


class NewUserForm(QDialog):

    def __init__(self, parent=None):
        super(NewUserForm, self).__init__(parent)
        self.createWidgets()
        self.layoutWidgets()
        self.createConnections()

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
        screenLayout.setRowMinimumHeight(8, 10)
        screenLayout.addWidget(self.buttonBox, 9, 3)
        screenLayout.setRowStretch(10, 1)

        self.setLayout(screenLayout)

    def createConnections(self):
        self.nextButton.clicked.connect(self.accepted)

    def accepted(self):
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


def main():
    app = QApplication(sys.argv)
    form = NewUserForm()
    form.showFullScreen()
    app.exec_()

if __name__ == "__main__":
    main()
