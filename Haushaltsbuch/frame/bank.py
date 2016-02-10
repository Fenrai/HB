from PyQt4.QtCore import QObject
from __builtin__ import dict

class BankFactory(object):
    def __init__(self):
        self.banks = []

    def getBank(self, blz=None, bic=None, name=None,):
        if blz:
            for bank in self.banks:
                if bank.getBLZ() == blz:
                    return bank
        elif bic:
            for bank in self.banks:
                if bank.getBIC() == bic:
                    return bank
        elif name:
            for bank in self.banks:
                if bank.getName() == name:
                    return bank
        bank = Bank(dict(name=name,
                         bic=bic,
                         blz=blz))
        self.banks.append(bank)
        return bank


class Bank(QObject):
    def __init__(self, data, parent=None):
        super(Bank, self).__init__(parent)
        self.name = data['name']
        self.bic = data['bic']
        self.blz = data['blz']

    def getBIC(self):
        return self.bic

    def getBLZ(self):
        return self.blz

    def getName(self):
        return self.name

    def __eq__(self, bank):
        if not isinstance(bank, Bank):
            return False
        if self.blz and bank.getBLZ() and self.blz == bank.getBLZ():
            return True
        elif self.bic and bank.getBIC() and self.bic == bank.getBIC():
            return True
        return False
