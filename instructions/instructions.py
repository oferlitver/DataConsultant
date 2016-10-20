# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *


__author__ = 'Ofer Litver'


class InstructionScreen(QDialog):

    def __init__(self):
        super(InstructionScreen, self).__init__()
        self.instructionText = self.importInstructions()
        print(self.instructionText)

        instructionLabel = QLabel(self.instructionText[0])
        layout = QHBoxLayout()
        layout.addWidget(instructionLabel)
        self.setLayout(layout)

    def importInstructions(self, filename="instructions.txt"):
        f = open(filename, 'r')
        res = f.readlines()
        f.close()
        return res


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ins = InstructionScreen()
    ins.show()
    app.exec_()