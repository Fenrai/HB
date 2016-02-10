from controller.controller import Controller



def main():
    controller = Controller()
    
    controller.readCSV('Kontoauszug.CSV')
    
    for transaction in controller.transactionFactory.transactions:
        print transaction.__dict__
        controller.model.db.addTransaction(transaction)


if __name__ == '__main__':
    main()