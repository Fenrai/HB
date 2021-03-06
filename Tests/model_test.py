#  -*- coding: latin-1 -*-

import time

from haushaltsbuch.model.model import Model

def main():
    model = Model()
    numbers = dict(
        account=1,
        bank=2,
        bic=4,
        iban=5)

    model.createNewAccount('test', 'desc', numbers)

    for account in model.getAccounts():
        print account.getOldAccountIdentifiers() + account.getNewAccountIndentifiers()

if __name__ == '__main__':
    main()
