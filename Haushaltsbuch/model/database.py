from os.path import exists, join, dirname, abspath
from os import makedirs, remove
from sqlite3 import connect


class SQLiteDatabase():
    def __init__(self):
        self.dataBase = join(dirname(abspath(__file__)),
                             'data', 'haushaltsbuch.sqlite')
        self.checkDatabase()

        self.db = connect(self.dataBase)

    def checkDatabase(self):
        if not exists(self.dataBase):
            self.createDatabase()

    def createDatabase(self):
        if not exists(join(dirname(abspath(__file__)), 'data')):
            makedirs(join(dirname(abspath(__file__)), 'data'))

        if exists(join(dirname(abspath(__file__)), 'data', 'haushaltsbuch.sqlite')):
            remove(join(dirname(abspath(__file__)), 'data', 'haushaltsbuch.sqlite'))

        db = connect(self.dataBase)

        cur = db.cursor()

        cur.execute('''CREATE TABLE banks (
                        bankid             INTEGER PRIMARY KEY,
                        name               CHAR(200),
                        bic                CHAR(11),
                        blz                CHAR(8)
                        );''')

        cur.execute('''CREATE TABLE accounts (
                        accountid          INTEGER PRIMARY KEY,
                        bank               INTEGER,
                        accountnumber      INTEGER,
                        iban               INTEGER,
                        FOREIGN KEY(bank) REFERENCES banks(bankid)
                        );''')

        cur.execute('''CREATE TABLE correspondents (
                        correspondentid    INTEGER PRIMARY KEY,
                        name               CHAR(200),
                        account            INTEGER,
                        description        CHAR(200),
                        FOREIGN KEY(account) REFERENCES accounts(accountid)
                        );''')

        cur.execute('''CREATE TABLE filters (
                        filterid           INTEGER PRIMARY KEY,
                        filterstring       CHAR(50),
                        subaccount         INTEGER,
                        FOREIGN KEY(subaccount) REFERENCES subaccounts(subaccountid)
                        );''')

        cur.execute('''CREATE TABLE accountingentries (
                        accountingid       INTEGER PRIMARY KEY,
                        accountingstring   CHAR(200)
                        );''')

        cur.execute('''CREATE TABLE subaccounts (
                        subaccountid       INTEGER PRIMARY KEY,
                        name               CHAR(50),
                        description        CHAR(200),
                        account            INTEGER,
                        FOREIGN KEY(account) REFERENCES accounts(accountid)
                        );''')

        cur.execute('''CREATE TABLE transactions (
                        transactionid      INTEGER PRIMARY KEY,
                        amount             REAL,
                        account            INTEGER,
                        correspondent      INTEGER,
                        issuedate          INTEGER,
                        executiondate      INTEGER,
                        purpose            CHAR(200),
                        accountingentry    CHAR(200),
                        notes              CHAR(200),
                        FOREIGN KEY(account) REFERENCES accounts(accountid),
                        FOREIGN KEY(accountingentry) REFERENCES accountingenties(accountingid),
                        FOREIGN KEY(correspondent) REFERENCES correspondents(correspondentid)
                        );''')

        cur.execute('''INSERT INTO banks(name, bic, blz)
                        VALUES('newbank', 'DENEWBANK', 70150000)''')

        cur.execute('''INSERT INTO accounts (bank, accountnumber, iban)
                        VALUES (1, 906113212, 'IBANTEST')''')

        cur.execute('''INSERT INTO transactions(amount, account, correspondent, issuedate,executiondate, purpose, accountingentry, notes)
                        values(2.5, 3, 4, 5, 6, 'reason', 8, "\'"); ''')

        cur.execute('''select * from transactions''')


        db.commit()
        db.close()

    def addTransaction(self, transaction):
        if self.getTransactionId(transaction):
            return

#         with connect(self.dataBase) as db:
        cur = self.db.cursor()
        cur.execute('''INSERT INTO transactions(amount, account, correspondent,
                                                issuedate,executiondate,
                                                purpose, accountingentry,
                                                notes)
                        values(%d, %d, %d, "%s", "%s", "%s", "%s", "%s");''' %
                        (transaction.amount,
                         1,  # self.getAccountId(transaction.account),
                         1,  # self.getCorrespondentId(transaction.correspondent),
                         transaction.issueDate,
                         transaction.executionDate,
                         transaction.purpose,
                         transaction.accountingEntry,
                         transaction.notes
                         )
                    )
        self.db.commit()

    def addBank(self, bank):
        if self.getBankId(bank):
            return

        with connect(self.dataBase) as db:
            cur = db.connect()
            cur.execute('''INSERT INTO bank
                            VALUES('%s', '%s', '%s');''' %
                            (bank.name,
                             bank.bic,
                             bank.blz)
                        )
            db.commit()

    def addAccount(self, account):
        if self.getAccountId(account):
            return
        with connect(self.dataBase) as db:
            cur = db.connect()
            cur.execute('''INSERT INTO accounts
                            VALUES(%d, %d, %d);''' %
                            (account.bank,
                             account.number,
                             account.iban
                             )
                        )

            db.commit()

    def addSubaccount(self, subaccount):
        if self.getSubAccountId(subaccount):
            return
        with connect(self.dataBase) as db:
            cur = db.connect()
            cur.execute('''INSERT INTO subaccounts
                            VALUES('%s', '%s', %d);''' %
                            (subaccount.name,
                             subaccount.description,
                             self.getAccountId(subaccount.account)
                             )
                        )

            db.commit()

# TBD
#     def addFilter(self, sfilter):
#         if self.getFilterId(sfilter):
#             return
#         with connect(self.dataBase) as db:
#             cur = db.connect()
#             cur.execute('''INSERT INTO
#                             VALUES();''' %
#                             (
#                              )
#                         )
#
#             db.commit()
#
#     def addCorrespondent(self, correspondent):
#         if self.getCorrespondentId(correspondent):
#             return
#         with connect(self.dataBase) as db:
#             cur = db.connect()
#             cur.execute('''INSERT INTO
#                             VALUES();''' %
#                             (
#                              )
#                         )
#
#             db.commit()
#
#     def addAccountingentry(self, accountingentry):
#         if self.getAccountingId(accountingentry):
#             return
#         with connect(self.dataBase) as db:
#             cur = db.connect()
#             cur.execute('''INSERT INTO
#                             VALUES();''' %
#                             (
#                              )
#                         )
#
#             db.commit()

    def getAccountId(self, account):
        return 1

    def getBankId(self, bank):
        return 1

    def getCorrespondentId(self, correspondent):
        return 1

    def getFilterId(self, sfilter):
        return 1

    def getSubAccountId(self, subaccount):
        return 1

    def getTransactionId(self, transaction):
        return 0

    def getAccountingId(self, accounting):
        return 1
