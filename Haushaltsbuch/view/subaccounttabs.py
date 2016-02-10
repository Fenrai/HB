from PyQt4.QtGui import QTabWidget
from view.monthwidget import MonthWidget


class SubAccountTabs(QTabWidget):
    def __init__(self, subAccounts, parent=None):
        super(SubAccountTabs, self).__init__(parent)

        for account in subAccounts:
            self.addSubAccount(account)

    def addSubAccount(self, account):
        self.addTab(MonthWidget, account.name)
