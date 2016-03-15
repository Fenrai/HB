#  -*- coding: latin-1 -*-

from haushaltsbuch.controller.controller import Controller
from os.path import join

def main():
    controller = Controller()

    controller.readCSV(join('..', 'test.CSV'))

    for transaction in controller.transactionFactory.transactions:
        print transaction.__dict__['correspondent'].name
        controller.model.db.addTransaction(transaction)


if __name__ == '__main__':
    main()
