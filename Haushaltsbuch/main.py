from PyQt4.QtGui import QApplication
import sys
from controller.controller import Controller

def main(argv=None):
    if not argv:
        argv = sys.argv

    app = QApplication(argv)

    _ = Controller()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
