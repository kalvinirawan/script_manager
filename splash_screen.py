

#===============================================================================
# IMPORT
import os
import sys

from Qt import QtWidgets, QtGui, QtCore, QtCompat

#===============================================================================
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]

#===============================================================================
# CLASS

class SplashScreen():   
    def __init__(self):
        # define ui path
        path_ui = ("/").join([os.path.dirname(__file__), 'ui', TITLE + '.ui'])
    
        # load ui
        self.wgUtil = QtCompat.loadUi(path_ui)
        
        # remove title bar
        self.wgUtil.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.wgUtil.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.wgUtil.show()



def start():
    app = QtWidgets.QApplication(sys.argv)
    classVar = SplashScreen()
    app.exec_()

start()