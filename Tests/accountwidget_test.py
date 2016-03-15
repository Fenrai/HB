#  -*- coding: latin-1 -*-

import sys

from PyQt4.QtGui import QApplication

from haushaltsbuch.view.accountwidget import AccountWidget

def main(argv=None):
    if not argv:
        argv = sys.argv

    app = QApplication(argv)
    window = AccountWidget()

    window.addTopLevelPeriod('2015')
    window.addSecondLevelPeriod('Januar')
    window.addSecondLevelPeriod('Februar')

    window.addTopLevelPeriod('2016')
    window.addSecondLevelPeriod('Januar')

    window.addNextMonth()

    window.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
