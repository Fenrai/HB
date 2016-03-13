#  -*- coding: latin-1 -*-

import os
from os.path import join, dirname, abspath

def getUiFile(name):
    return join(dirname(abspath(__file__)), 'ui', '%s.ui' % name)

def inquireAccountData():
    pass