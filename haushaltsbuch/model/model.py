#  -*- coding: latin-1 -*-

import sqlite3
from os import makedirs, remove
from os.path import exists, join, abspath, dirname

from PyQt4.QtCore import QObject

from haushaltsbuch.frame.account import Account
from haushaltsbuch.model.database import SQLiteDatabase

class Model(QObject):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.accounts = []

        self.db = SQLiteDatabase()


    def loadLastSession(self):
        pass

    def createNewAccount(self, name, description, numbers):
        account = Account(name, description, numbers)
        self.addNewAccount(account)

        return account

    def addNewAccount(self, account):
        self.accounts.append(account)

    def getAccounts(self):
        return self.accounts

    def accountExists(self, identifiers):
        if identifiers['old']:
            ids = identifiers['old']
            for account in self.accounts:
                if account.getOldIdentifiers() == ids:
                    return account
        else:
            ids = identifiers['new']
            for account in self.accounts:
                if account.getNewIdentifiers() == ids:
                    return account

    def save(self):
        pass

    def load(self):
        pass

    def importCSV(self, path):
        pass
