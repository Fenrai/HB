class BaseModel():
    def __init__(self):
        pass
    
    
    # gather data from model and generate a list of transactions with it.
    def getTransactions(self, account, fromTo, subaccount=None):
        # account: Mainaccount
        # fromTo: [fromDate, toDate]
        # subaccount: if None: all transactions
        # return: [Transactions]
        pass
    
    # extract data from 'transaction' and persistently save it to the model.
    def updateTransaction(self, transaction):
        # transaction: Transactionn
        pass
    
    # extract data from new 'transaction' and psersistently save it to the model.
    def createTransactionDataSet(self, transaction):
        # transaction: Transaction
        pass