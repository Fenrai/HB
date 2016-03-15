#  -*- coding: latin-1 -*-

from os.path import join

from haushaltsbuch.controller.csvreader import readStatement
from haushaltsbuch.frame.bank import BankFactory

def main():
#     banks = BankFactory()
    rawTransactions = readStatement(join('..', 'test.CSV'), ';')
    for transaction in rawTransactions:
        print transaction

#     print '-----'
#     for bank1 in banks.banks:
#         for bank2 in banks.banks:
#             if bank1 == bank2:
#                 print bank1 is bank2
#
#     print '-----'


if __name__ == '__main__':
    main()

