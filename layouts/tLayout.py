# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLayout

__author__ = 'Ofer Litver'

class ItemWrapper(object):
    def __init__(self,j i, p):
        self.item = i
        self.position = p


class TLayout(QLayout):

    def __init__(self):
        super(TLayout, self).__init__()

        self.lst = []

    def addWidget(self, widget, position):
        self.add(QWidgetItem(widget), position)

    def add(self, item, position):
        self.lst.append(ItemWrapper(item, position))

if __name__ == '__main__':
    t = TLayout()
    l = QLabel("test label")
    t.addWidget(l, TLayout.Top)
