# -*- coding: utf-8 -*-
__author__ = 'Ofer'

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setWindowTitle("User details")
        
    def create_widgets(self):
        self.idLabel = QLabel("Identification number")
        self.idLineEdit = QLineEdit()
        # TODO add validation
        regexp = QRegExp('^\d{8,9}$')
        validator = QRegExpValidator(regexp)
        self.idLineEdit.setValidator(validator)
        #self.idLineEdit.setPlaceholderText("Please type your ID")
        
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
                      "Mechanical Engineering", 
                      "Industrial Engineering", 
                      "Biomedical Engineering", 
                      "Environmental Engineering"]
        self.fieldComboBox = QComboBox()
        self.fieldComboBox.addItems(field_list)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
    def layout_widgets(self):
        grid = QGridLayout()
        grid.addWidget(self.idLabel, 0, 0)
        grid.addWidget(self.idLineEdit, 0, 1)
        grid.addWidget(self.ageLabel, 1, 0)
        grid.addWidget(self.ageSpinBox, 1, 1)
        grid.addWidget(self.genderLabel, 2, 0)
        grid.addLayout(self.genderLayout, 2, 1)
        grid.addWidget(self.fieldLabel, 3, 0)
        grid.addWidget(self.fieldComboBox, 3, 1)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)
        # self.reject.connect(self.rejected())
        
    def accepted(self):
        # get value of gender checkbox
        g = self.genderButtonGroup.checkedId()
        gender = 'm' if g == 1 else 'f' if g == 2 else '-'
        
        # write results to CSV file
        file = open("data.csv", "w")
        file.write(self.idLineEdit.text() +
                   ',' +
                   str(self.ageSpinBox.value()) +
                   ',' + 
                   gender)
        file.close()
        #print self.fieldComboBox.currentText()
        #print self.fieldComBox.

    def rejected(self):
        self.closeEvent(self)
    
    def closeEvent(self, event):
        """in case of a click on X"""
        reply = QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
