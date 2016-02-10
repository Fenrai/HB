from os.path import join
import os

def getUiFile(name):
    return join(os.path.dirname(os.path.abspath(__file__)), 'ui', '%s.ui' % name)

def inquireAccountData():
    pass