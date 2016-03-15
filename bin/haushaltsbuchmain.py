#  -*- coding: latin-1 -*-

import sys
from os.path import join, dirname

from PyQt4.QtGui import QApplication

sys.path.append(join(dirname(__file__), '..'))
from haushaltsbuch.controller.controller import Controller

def main(argv=None):
    if not argv:
        argv = sys.argv

    app = QApplication(argv)

    _ = Controller()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
