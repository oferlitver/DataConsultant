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

        self.setWindowTitle("User details")

    def createWidgets(self):
        self.title = QLabel("Welcome")
        titleFont = QFont()
        titleFont.setPointSize(36)
        self.title.setFont(titleFont)
        self.subtitle = QLabel("Please fill the following details:")

        self.idLabel = QLabel("Identification number")
        self.idLineEdit = QLineEdit()
        # TODO add validation
        regexp = QRegExp('^\d{8,9}$')
        validator = QRegExpValidator(regexp)
        self.idLineEdit.setValidator(validator)

        self.ageLabel = QLabel("Age:")
        self.ageSpinBox = QSpinBox()
        self.ageSpinBox.setRange(16, 80)
        self.ageSpinBox.setValue(20)

        self.genderLabel = QLabel("Gender:")
        self.maleRadioButton = QRadioButton("Male")
        self.femaleRadioButton = QRadioButton("Female")
        self.genderButtonGroup = QButtonGroup()
        self.genderButtonGroup.addButton(self.maleRadioButton, 1)
        self.genderButtonGroup.addButton(self.femaleRadioButton, 2)
        self.genderLayout = QHBoxLayout()
        self.genderLayout.addWidget(self.maleRadioButton)
        self.genderLayout.addWidget(self.femaleRadioButton)

        self.fieldLabel = QLabel("Primary field of studies:")
        field_list = ["--- Please select ---",
                      "Electrical Engineering",
                      "9echanical Engineering",
                      "Industrial Engineering",
                      "Biomedical Engineering",
                      "Environmental Engineering"]
        self.fieldComboBox = QComboBox()
        self.fieldComboBox.addItems(field_list)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                          QDialogButtonBox.Cancel)

    def layoutWidgets(self):
        screenLayout = QGridLayout()
        screenLayout.setColumnStretch(0, 1)
        screenLayout.setColumnStretch(2, 1)
        screenLayout.setRowStretch(0, 1)
        screenLayout.setRowStretch(1, 1)
        screenLayout.setRowStretch(2, 1)
        
        centerLayout = QGridLayout()
        centerLayout.addWidget(self.title, 0, 0, 1, 2)
        centerLayout.setRowStretch(0, 2)
        centerLayout.addWidget(self.subtitle, 1, 0, 1, 2)
        centerLayout.addWidget(self.idLabel, 2, 0)
        centerLayout.addWidget(self.idLineEdit, 2, 1)
        centerLayout.addWidget(self.ageLabel, 3, 0)
        centerLayout.addWidget(self.ageSpinBox, 3, 1)
        centerLayout.addWidget(self.genderLabel, 4, 0)
        centerLayout.addLayout(self.genderLayout, 4, 1)
        centerLayout.addWidget(self.fieldLabel, 5, 0)
        centerLayout.addWidget(self.fieldComboBox, 5, 1)

        screenLayout.addLayout(centerLayout, 1, 1)
        self.setLayout(screenLayout)

    def createConnections(self):
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)

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
