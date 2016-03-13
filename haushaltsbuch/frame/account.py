#  -*- coding: latin-1 -*-

from haushaltsbuch.frame.correspondent import CorrespondentFactory
from haushaltsbuch.frame.transaction import TransactionFactory

class AccountFactory(object):
    def __init__(self):
        self.accounts = []
        self.ownaccounts = []

    def getAccount(self, name, description, numbers):
        for account in self.accounts:
            if account.matches(numbers):
                return account
        account = Account(name, description, numbers)
        self.accounts.append(account)
        return account

    def getOwnAccount(self, number):
        for account in self.ownaccounts:
            if account.accountNumber == number:
                return account

        return None

    def createOwnAccount(self, data):
        pass

class Account():
    def __init__(self, name, description, numbers):
        self.name = name
        self.description = description
        self.accountNumber = numbers['account']
        self.bankCode = numbers['bank']
        self.iban = numbers['iban']
        self.bic = numbers['bic']
        self.correpondents = CorrespondentFactory()
        self.transactions = TransactionFactory()
        self.notes = ''

    def matches(self, numbers):
        return (self.getOldAccountIdentifiers() == (numbers['account'],
                                                     numbers['bank'])
                or self.getNewAccountIndentifiers() == (numbers['iban'],
                                                        numbers['bic']))

    def getOldAccountIdentifiers(self):
        return(self.accountNumber, self.bankCode)

    def getNewAccountIndentifiers(self):
        return (self.iban, self.bic)

class SubAccount():
    def __init__(self, pattern, name, description):
        self.pattern = pattern
        self.name = name
        self.description = description

class ownAccount(Account):
    def __init__(self, description, numbers):
        super(ownAccount)

    def addTransaction(self, data):
        data['transaction']['correspondent'] = \
            self.correpondents.getCorrespondent(data['correspondent'])
        self.transactions.getTransaction(data['transaction'])

    def filterTransactions(self, criteria):
        if criteria[0] == 'sub':
            pass
        elif criteria[0] == 'month':
            pass
        elif criteria[0] == 'correspondent':
            pass
