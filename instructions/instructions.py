# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



__author__ = 'Ofer Litver'


class InstructionScreen(QDialog):

    def __init__(self):
        super(InstructionScreen, self).__init__()
        self.instructionText = self.importInstructions()

        instructionLabel = QLabel(self.instructionText)
        instructionLabel.setWordWrap(True)
        instructionLabel.setFixedSize(360, 240)

        layout = QHBoxLayout()
        layout.addWidget(instructionLabel)
        self.setLayout(layout)

    def importInstructions(self, filename="instructions.txt"):
        f = open(filename, 'r')
        res = f.read()
        f.close()
        return res


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ins = InstructionScreen()
    ins.showFullScreen()
    app.exec_()