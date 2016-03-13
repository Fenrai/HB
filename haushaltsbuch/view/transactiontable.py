#  -*- coding: latin-1 -*-

import random
from datetime import date

from PyQt4.QtCore import pyqtSignal, Qt
from PyQt4.QtGui import QTableWidget, QTableWidgetItem

from haushaltsbuch.frame.transaction import Transaction

class TransactionTable(QTableWidget):
    ISSUE = 0
    EXECUTION = 1
    CORRESPONDENT = 2
    AMOUNT = 3
    PURPOSE = 4
    ACCOUNTING = 5

    rowAdded = pyqtSignal()


    def __init__(self, parent=None):
        super(TransactionTable, self).__init__(parent)

        self.optimizeColumnWidths()

    def getProgress(self):
        total = 0
        for row in range(self.rowCount()):
            total += int(self.item(row, self.AMOUNT).text())

        return total

    def addRow(self, transaction=None):
        if not transaction:
            transaction = Transaction({'amount' : 30,
                                       'purpose' : 'purpose',
                                       'correspondent':'correspondent',
                                       'issueDate' : date(2015, 6, 14),
                                       'executionDate' : date(2015, 8, 17),
                                       'accountingEntry':'accounting'})
        row = self.rowCount()
        self.insertRow(row)
        items = [QTableWidgetItem(str(transaction.issueDate)),
                QTableWidgetItem(str(transaction.executionDate)),
                QTableWidgetItem(transaction.correspondent),
                QTableWidgetItem(str(transaction.amount)),
                QTableWidgetItem(transaction.purpose),
                QTableWidgetItem(transaction.accountingEntry)]

        for item, column in zip(items, self.getColumnAliases()):
            if column not in [self.PURPOSE]:
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.setItem(row, column, item)

        self.optimizeColumnWidths()

        self.rowAdded.emit()

    def setColumnVisibility(self, visibility=None):
        if not visibility:
            visibility = [random.choice([True, False]) for _ in range(6)]
        for visible, column in zip(visibility, self.getColumnAliases()):
                self.setColumnHidden(column, not visible)

        self.optimizeColumnWidths()

    def optimizeColumnWidths(self):
        self.resizeColumnsToContents()
        self.horizontalHeader().setStretchLastSection(True)

    def getColumnAliases(self):
        return [self.ISSUE,
                self.EXECUTION,
                self.CORRESPONDENT,
                self.AMOUNT,
                self.PURPOSE,
                self.ACCOUNTING]
