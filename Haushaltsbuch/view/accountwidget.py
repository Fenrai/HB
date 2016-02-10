from PyQt4.QtGui import QWidget, QTreeWidgetItem
from PyQt4 import uic
from view import getUiFile, monthwidget
from view.monthwidget import MonthWidget
from view.datetree import MonthItem



class AccountWidget(QWidget):
    def __init__(self, parent=None):
        super(AccountWidget, self).__init__(parent)

        # codeCompletionBlock start
        from PyQt4.QtGui import QTreeWidget, QStackedWidget
        self.dateTree = QTreeWidget()
        self.monthStack = QStackedWidget()
        # codeCompletionBlock end

        uic.loadUi(getUiFile('AccountWidget'), self)

        self.dateTree.currentItemChanged.connect(self.syncronizeStack)

        self.addTopLevelPeriod('CurrentTotal')

    def addNewSubaccount(self):
        data = self.inquireSubaccountData()
        print self

    def inquireSubaccountData(self):
        pass
    
    def addNextMonth(self):
        # treewidget get toplevel items
        # find last item
        # add new toplevvelitem if  toplevel item has 12 subitems
        # add new sublevel item
        
        last = self.getLastItem()
        
        month = last.monthwidget
        self.dateTree.addMonth(month)


    def addSecondLevelPeriod(self, text):
        # TODO: find previous item
        item = self.dateTree.currentItem()
        if item:
            item.addChildren([QTreeWidgetItem([text])])
            self.monthStack.addWidget(MonthWidget())
            print self.getLastItem()
    
    def getLastItem(self):
        return MonthItem(1, MonthWidget())

    def addTopLevelPeriod(self, text):
        self.monthStack.addWidget(MonthWidget())
        item = QTreeWidgetItem([text])
        self.dateTree.addTopLevelItem(item)
        self.dateTree.setCurrentItem(item)

    def syncronizeStack(self, item):
        print item
#         self.monthStack.setCurrentIndex(item.getIndex())

