#  -*- coding: latin-1 -*-

from PyQt4.QtCore import QObject

class SubaccountFactory():
    def __init__(self):
        self.subaccounts = []

    def getSubaccount(self, name):
        for subaccount in self.subaccounts:
            if subaccount.name == name:
                return subaccount
        return SubAccount(dict(name=name,
                               description='',
                               account=''))


class SubAccount(QObject):
    def __init__(self, data, parent=None):
        super(SubAccount, self).__init__(parent)
        self.name = data['name']
        self.description = data['description']
        self.account = data['account']

    def editName(self, name):
        self.name = name

    def editDescription(self, description):
        self.description = description

    def editAccount(self, account):
        self.account = account
