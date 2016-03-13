#  -*- coding: latin-1 -*-

from PyQt4.QtCore import QObject
from haushaltsbuch.model.model import Model
from haushaltsbuch.view.mainwindow import MainWindow
from haushaltsbuch.frame.account import Account, AccountFactory
from haushaltsbuch.frame.bank import Bank, BankFactory
from haushaltsbuch.frame.subaccount import SubaccountFactory
from haushaltsbuch.frame.correspondent import CorrespondentFactory
from haushaltsbuch.controller import CACCOUNT, CNAME, CBANKCODE, CIBAN, \
    CBIC, ACCOUNT, AMOUNT, PURPOSE, ISSUEDATE, EXECDATE, ACCENTRY, INFO, \
    csvreader
from haushaltsbuch.frame.transaction import TransactionFactory

class Controller(QObject):
    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)

        self.model = Model()
        self.createFactories()
#         self.view = MainWindow()
#
#         self.view.show()

    def createFactories(self):
        self.bankFactory = BankFactory()
        self.accountFactory = AccountFactory()
        self.subaccountFactory = SubaccountFactory()
        self.correspondentFactory = CorrespondentFactory()
        self.transactionFactory = TransactionFactory()

    def getTransactions(self, account, start, end):
        pass

    def inquireAccountData(self):
        return {'name': 'Account A',
                'description': 'genericAccount',
                'numbers': {'account': 1,
                            'bank': 2,
                            'iban': 3,
                            'bic': 4}}

    def createNewAccount(self):
        data = self.inquireAccountData()
        account = Account(data['name'], data['description'], data['numbers'])
        self.model.addNewAccount(account)
        self.view.addNewAccount(account)

    def readCSV(self, csvpath):
        entries = csvreader.readStatement(csvpath)
        for entry in entries:
            cdata = dict(
                name=entry[CNAME],
                accountNumber=entry[CACCOUNT],
                bankCode=entry[CBANKCODE],
                iban=entry[CIBAN],
                bic=entry[CBIC])
            correspondent = self.correspondentFactory.getCorrespondent(cdata)
            tdata = dict(
                account=entry[ACCOUNT],
                amount=entry[AMOUNT],
                purpose=entry[PURPOSE],
                correspondent=correspondent,
                issueDate=entry[ISSUEDATE],
                executionDate=entry[EXECDATE],
                accountingEntry=entry[ACCENTRY],
                info=entry[INFO])

            self.transactionFactory.getTransaction(tdata)


