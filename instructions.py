# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QHBoxLayout, QDialog, QApplication
from PyQt5.QtGui import QFont


__author__ = 'Ofer Litver'


class InstructionsScreen(QDialog):

    def __init__(self, filename="./instructions/instructions.txt"):
        super(InstructionsScreen, self).__init__()

        # create label
        self.instructionsLabel = QLabel()
        self.instructionsLabel.setWordWrap(True)
        self.instructionsLabel.setMaximumWidth(800)
        self.instructionsLabel.setFont(QFont("Helvetica", 14))
        self.importInstructions(filename=filename)

        layout = QHBoxLayout()
        layout.addWidget(self.instructionsLabel)
        self.setLayout(layout)

    def importInstructions(self, filename):
        f = open(filename, 'r')
        self.instructionsLabel.setText(f.read())
        f.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ins = InstructionsScreen()
    ins.showFullScreen()
    app.exec_()