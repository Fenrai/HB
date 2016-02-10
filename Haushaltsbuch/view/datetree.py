#*-*encoding = utf8*-*

from PyQt4.QtGui import QTreeWidget, QTreeWidgetItem
from PyQt4.QtCore import pyqtSignal
from PyQt4.Qt import QString

months = {
    1: 'Januar',
    2: 'Februar',
    3: 'Maerz',
    4: 'April',
    5: 'Mai',
    6: 'Juni',
    7: 'Juli',
    8: 'August',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Dezember',
}


class DateTree(QTreeWidget):
    def __init__(self, parent=None):
        super(DateTree, self).__init__(parent)
    
    def addYear(self):
        lastYear = self.topLevelItem(self.topLevelItemCount()).year
        currentYear = YearItem(lastYear + 1)
        self.addTopLevelItem(currentYear)
        
        return currentYear
        
    def addMonth(self, monthWidget):
        print self.topLevelItemCount()
        lastYear = self.topLevelItem(self.topLevelItemCount()-1)
        if lastYear.canAddMonth():
            lastYear.addMonth(monthWidget)
        else:
            self.addYear().addMonth(monthWidget)


class YearItem(QTreeWidgetItem):    
    def __init__(self, year, item=None, parent=None):
        super(YearItem, self).__init__(parent)
        self.children = []
        self.previousTopLevelItem = item
        if isinstance(year, int):
            self.year = year
            self.setText(str(year))
        else:
            self.year = None
        
    def addMonth(self, child):
        self.children.append(child)
        return self.addChild(child)
    
    def getlastMonth(self):
        if len(self.children):
            return self.child(len(self.children))
        else:
            return self.previousTopLevelItem.getlastChild()
    
    def canAddMonth(self):
        return len(self.children) <= 12
        
    
class MonthItem(QTreeWidgetItem):
    def __init__(self, month, widget, parent=None):
        super(MonthItem, self).__init__(parent)
        self.setText(0,QString(months[month]))
        self.monthwidget = widget