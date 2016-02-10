from pprint import pprint
class TransactionFactory(object):
    def __init__(self, parent=None):
        self.transactions = []  # TODO: preselection(date?)

    def getTransaction(self, data):
        '''
            return existing transaction matching the data provided or
            return a new transaction.
        '''
        for transaction in self.transactions:
            if transaction.matches(data):
                return transaction
        transaction = Transaction(data)
        self.transactions.append(transaction)
        return transaction


class Transaction(object):
    """
        Object holding all the info regarding a single transaction
    """
    def __init__(self, data, parent=None):
        super(Transaction, self).__init__()
        self.account = data['account']
        self.amount = data['amount']
        self.purpose = data['purpose']
        self.correspondent = data['correspondent']
        self.issueDate = data['issueDate']
        self.executionDate = data['executionDate']
        self.accountingEntry = data['accountingEntry']
        self.info = data['info']
        self.purpose = data['purpose']
        self.notes = data['notes'] if 'notes' in data.keys() else ''

    def matches(self, data):
        if (data['amount'] == self.amount
                and data['correspondent'] == self.correspondent
                and data['issueDate'] == self.issueDate
                and data['executionDate'] == self.executionDate
                and data['accountingEntry'] == self.accountingEntry):
            return True

        return False

