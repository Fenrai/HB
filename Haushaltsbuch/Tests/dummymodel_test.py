from model.model_dummy import Model
from frame import account
from frame.account import AccountFactory

def main():
    model = Model()
    accounts = AccountFactory()
    
    account = accounts.getAccount('Test', 'Test Acount',
                                  {"accountNumber": 123456678,
                                   "bankCode": 98765432,
                                   "iban": 'DE123456789',
                                   "bic": '987654321XXX',
                                    })
    
    print model.getTransactions(account, ((10, 2015), (11, 2015)), '')


if __name__ == '__main__':
    main()
