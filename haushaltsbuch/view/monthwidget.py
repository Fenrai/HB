#  -*- coding: latin-1 -*-

from PyQt4.QtGui import QWidget
from PyQt4 import uic
from haushaltsbuch.view import getUiFile
from haushaltsbuch.view.transactiontable import TransactionTable


class MonthWidget(QWidget):
    def __init__(self, previous=None, parent=None):
        super(MonthWidget, self).__init__(parent)

        # codeCompletionBlock start
        from PyQt4.QtGui import QDoubleSpinBox
        spinBox = QDoubleSpinBox()
        self.spinBoxClosing = spinBox
        self.spinBoxOpening = spinBox
        self.spinBoxProgress = spinBox
        self.tableTransactions = TransactionTable()
        # codeCompletionBlock end

        uic.loadUi(getUiFile('MonthWidget'), self)

        self.previous = previous

        if self.previous:
            self.updateOpeningBalance()
            self.previous.spinBoxClosing.valueChanged.connect(self.updateOpeningBalance)

        self.tableTransactions.rowAdded.connect(self.updateSecondaryBalances)
        self.spinBoxOpening.valueChanged.connect(self.updateSecondaryBalances)


#         self.pushButton.clicked.connect(self.tableTransactions.addRow)
#         self.pushButton_2.clicked.connect(self.tableTransactions.setColumnVisibility)

    def getClosingBalance(self):
        return self.spinBoxClosing.value()

    def updateOpeningBalance(self):
        self.spinBoxOpening.setValue(self.previous.getClosingBalance())

    def updateSecondaryBalances(self):
        progress = self.tableTransactions.getProgress()
        self.spinBoxProgress.setValue(progress)
        self.spinBoxClosing.setValue(self.spinBoxOpening.value() - progress)

