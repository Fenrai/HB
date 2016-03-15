#  -*- coding: latin-1 -*-

import sys

from PyQt4.QtGui import QApplication

from haushaltsbuch.view.monthwidget import MonthWidget

def main(argv=None):
    if not argv:
        argv = sys.argv

    app = QApplication(argv)
    window = MonthWidget()
    window2 = MonthWidget(window)

    window.show()
    window2.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main(sys.argv))