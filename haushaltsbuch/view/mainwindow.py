

from PyQt4 import uic
from PyQt4.QtGui import QMainWindow

from haushaltsbuch.view import getUiFile, inquireAccountData
from haushaltsbuch.view.accountwidget import AccountWidget
from haushaltsbuch.model.model import Model

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # codeCompletionBlock start
        from PyQt4.QtGui import QComboBox, QToolButton, QStackedWidget

        self.accountSelection = QComboBox()
        self.accountButton = QToolButton()
        self.accountStack = QStackedWidget()
        # codeCompletionBlock end

        uic.loadUi(getUiFile('MainWindow'), self)

        self.model = Model()
        self.model.loadLastSession()

        self.actionAdd_Account.triggered.connect(self.addSubAccount)
        self.accountSelection.currentIndexChanged.connect(self.accountStack.setCurrentIndex)

    def addSubAccount(self):
        data = inquireAccountData()
        account = self.model.createNewAccount(data['name'],
                                              data['description'],
                                              data['numbers'])
        self.model.addNewAccount(account)

        self.accountSelection.addItem(account.description)
        self.accountStack.addWidget(AccountWidget())
