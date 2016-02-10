from . import BaseModel
from frame.transaction import TransactionFactory

class Model(BaseModel):
    def __init__(self):
        pass
    
    def getTransactions(self, account, fromTo, subaccount=None):
        BaseModel.getTransactions(self, account, fromTo, subaccount=subaccount)
        return self.convertToTransactions(self.getData(account, fromTo, subaccount))
    
    def getData(self, account, fromTo, subaccount):
        if subaccount:
            return [{"amount": 500,
                     "purpose": "dataset with subaccount",
                     "correspondent": {"name": "SubaccountCorrespondent",
                                       "accountnumber": 940349162,
                                       "bankCode": 72914418,
                                       "iban": None,
                                       "bic": None},
                     "issueDate": 1448195808,
                     "executionDate": 1448195808,
                     "accountingEntry": "test",
                     "usage": "",
                     "info": "",
                     "notes": "",}]
        
        else:
            return [{"amount": 500,
                     "purpose": "dataset with subaccount",
                     "correspondent": {"name": "SubaccountCorrespondent",
                                       "accountnumber": 940349162,
                                       "bankCode": 72914418,
                                       "iban": None,
                                       "bic": None},
                     "issueDate": 1448195808,
                     "executionDate": 1448195808,
                     "accountingEntry": "test",
                     "usage": "",
                     "info": "",
                     "notes": "",},
                    {"amount": 500,
                     "purpose": "dataset without subaccount",
                     "correspondent": {"name": "SubaccountCorrespondent",
                                       "accountnumber": 940349162,
                                       "bankCode": 72914418,
                                       "iban": "DE24178483834242215",
                                       "bic": "57892270XXX"},
                     "issueDate": 1448095808,
                     "executionDate": 1448125808,
                     "accountingEntry": "test",
                     "usage": "",
                     "info": "",
                     "notes": "",}]
    
    def convertToTransactions(self, data):
        return [TransactionFactory(dataSet) for dataSet in data]