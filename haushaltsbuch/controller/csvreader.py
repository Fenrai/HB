# -*- coding: latin-1 -*-

from csv import reader

def readStatement(filename, delimit=';'):
    rawTransactions = []
    with open(filename) as f:
        fileReader = reader(f, delimiter=delimit)
        for entry in fileReader:
            rawTransactions.append(entry)

    csvtype = getCsvType(rawTransactions[0])

    if csvtype == 1:
        return processRawTransactions1(rawTransactions)

    return []

def getCsvType(entry):
    '''
    for future additions
    '''
    if entry == ['Auftragskonto', 'Buchungstag', 'Valutadatum', 'Buchungstext',
                 'Verwendungszweck', 'Beguenstigter/Zahlungspflichtiger',
                 'Kontonummer', 'BLZ', 'Betrag', 'Waehrung', 'Info']:
        return 1

    return 0

def processRawTransactions1(rawTransactions):
    '''
    'Auftragskonto', 'Buchungstag', 'Valutadatum', 'Buchungstext', 'Verwendungszweck', 'Beguenstigter/Zahlungspflichtiger', 'Kontonummer', 'BLZ', 'Betrag', 'Waehrung', 'Info']
    '''

    for entry in rawTransactions:
        try:
            entry[0] = int(entry[0])
        except ValueError:
            entry[8:8] = ['IBAN', 'BIC']
            continue
        for i in range(1, len(entry)):
            entry[i] = convertValue(entry[i])

        if isinstance(entry[6], int) or entry[6] == '':
            entry[8:8] = ['', '']
        else:
            entry[6:6] = ['', '']

    return rawTransactions[1:]


def convertValue(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return value
