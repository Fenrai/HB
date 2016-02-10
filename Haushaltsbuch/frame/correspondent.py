class CorrespondentFactory(object):
    def __init__(self):
        self.correnpondents = []

    def getCorrespondent(self, data):
        for correspondent in self.correnpondents:
            if correspondent.matches(data):
                return correspondent
        correspondent = Correspondent(data)
        self.correnpondents.append(correspondent)
        return correspondent

class Correspondent(object):
    def __init__(self, data):
        super(Correspondent, self).__init__()
        self.name = data['name']
        self.accountNumber = data['accountNumber']
        self.bankCode = data['bankCode']
        self.iban = data['iban']
        self.bic = data['bic']

    def matches(self, data):
        return data == self.extractData()
    
    def extractData(self):
        return {"name": self.name,
                "accountNumber": self.accountNumber,
                "bankCode": self.bankCode,
                "iban": self.iban,
                "bic": self.bic}
