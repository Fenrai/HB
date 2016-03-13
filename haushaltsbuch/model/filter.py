#  -*- coding: latin-1 -*-

from PyQt4.QtCore import QObject


class Filter(QObject):
    def __init__(self, data, parent=None):
        super(Filter, self).__init__(parent)
        self.filterString = data['string']