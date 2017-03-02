#-*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QLabel, QLineEdit, QSpinBox, QRadioButton,
                             QButtonGroup, QHBoxLayout, QComboBox, QGridLayout,
                             QMessageBox, QApplication, QWidget)
from PyQt5.QtGui import QFont, QRegExpValidator, QPixmap
from PyQt5.QtCore import QRegExp
import config

# TODO finish this
#from DataConsultant.styles import styles


__author__ = 'Ofer Litver'


class ExperimentSetup(QWidget):
    """ Class for setting-up the experiment: choosing condition"""

    def __init__(self, parent=None):
        super(ExperimentSetup, self).__init__(parent)
        self.title = QLabel("EXPERIMENTER ONLY")
        # titleFont = QFont()
        # titleFont.setPointSize(36)
        # titleFont.setItalic(True)
        # self.title.setFont(titleFont)
        import os
        print(os.getcwd())
        self.mypixmap = QPixmap(os.getcwd() + "/ido.jpg")
        self.title.setPixmap(self.mypixmap)
        self.title.setGeometry(10, 10, 10, 10)

        # conditions list
        self.conditions_combo = QComboBox()
        conditions_list = config.CONDITIONS['condition']
        self.conditions_combo.addItems(conditions_list)

        # layout
        formLayout = QGridLayout()
        formLayout.setSpacing(20)
        formLayout.setColumnStretch(0, 5)
        formLayout.setColumnStretch(1, 2)
        formLayout.setColumnStretch(2, 5)
        formLayout.setRowStretch(0, 1)
        formLayout.setRowStretch(3, 1)

        formLayout.addWidget(self.title, 1, 1, 1, 2)
        formLayout.setRowMinimumHeight(2, 5)
        formLayout.addWidget(self.conditions_combo, 2, 1)

        self.setLayout(formLayout)


class NewUserForm(QWidget):

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
                      "Electrical Engineering & Computer Science",
                      "Electrical Engineering & Physics",
                      "Mechanical Engineering",
                      "Industrial Engineering",
                      "Biomedical Engineering",
                      "Environmental Engineering"]
        self.fieldComboBox = QComboBox()
        self.fieldComboBox.addItems(field_list)
        self.fieldLabel.setBuddy(self.fieldComboBox)

        # self.next_button = QPushButton("Next >")
        # self.buttonBox = QDialogButtonBox(self.next_button)

    def layoutWidgets(self):
        formLayout = QGridLayout()
        formLayout.setSpacing(20)
        formLayout.setColumnStretch(0, 5)
        formLayout.setColumnStretch(1, 2)
        formLayout.setColumnStretch(2, 2)
        formLayout.setColumnStretch(4, 5)
        formLayout.setRowStretch(0, 1)
        
        formLayout.addWidget(self.title, 1, 1, 1, 2)
        formLayout.setRowMinimumHeight(2, 50)
        formLayout.addWidget(self.subtitle, 3, 1, 1, 2)
        formLayout.addWidget(self.idLabel, 4, 1)
        formLayout.addWidget(self.idLineEdit, 4, 2)
        formLayout.addWidget(self.ageLabel, 5, 1)
        formLayout.addWidget(self.ageSpinBox, 5, 2)
        formLayout.addWidget(self.genderLabel, 6, 1)
        formLayout.addLayout(self.genderLayout, 6, 2)
        formLayout.addWidget(self.fieldLabel, 7, 1)
        formLayout.addWidget(self.fieldComboBox, 7, 2)
        formLayout.setRowMinimumHeight(8, 30)
        # formLayout.addWidget(self.next_button, 9, 2)
        formLayout.setRowStretch(10, 1)

        self.setLayout(formLayout)

    def createConnections(self):
        # self.next_button.clicked.connect(self.accepted)
        pass

    def accepted(self):
        pass

    def save_results(self):
        # get value of gender checkbox and convert
        # 1 --> m
        # 2 --> f
        g = self.genderButtonGroup.checkedId()
        # save variables to global module 'config'
        config.id = self.idLineEdit.text()
        config.age = self.ageSpinBox.value()
        config.male = 1 if g == 1 else 0 if g == 2 else 999
        config.field = self.fieldComboBox.currentText()

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
