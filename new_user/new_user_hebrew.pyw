# -*- coding: utf-8 -*-
__author__ = 'Ofer'

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        #self.create_connections()
        self.setWindowTitle(u"פרטי משתתף")
        
    def create_widgets(self):
        self.idLabel = QLabel(u"מספר תעודת-זהות:")
        
        self.idLineEdit = QLineEdit()
        #self.idLineEdit.setPlaceholderText("Please type your ID")
        
        self.ageLabel = QLabel(u"גיל:")
        
        self.ageSpinBox = QSpinBox()
        self.ageSpinBox.setAlignment(Qt.AlignRight)
        
    def layout_widgets(self):
        grid = QGridLayout()
        grid.addWidget(self.idLabel, 0, 1)
        grid.addWidget(self.idLineEdit, 0, 0)
        grid.addWidget(self.ageLabel, 1, 1)
        grid.addWidget(self.ageSpinBox, 1, 0)
        self.setLayout(grid)
        self.ageSpinBox.setFocus()

    #def create_connections(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()