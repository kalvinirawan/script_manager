#===============================================================================
# content                 = Basic UI for Nuke script manager
# version                 = 0.0.1
# date                    = 2019-12-03
#
# dependencies            = Qt
# author                  = Kalvin Irawan
#===============================================================================


#===============================================================================
# IMPORT
import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat

#===============================================================================
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]

#===============================================================================
# CLASS
class ScriptManager():

    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__), "ui", TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTON
        self.wgUtil.btnHelp.clicked.connect(self.press_help)
        self.wgUtil.btnSave.clicked.connect(self.press_save)
        self.wgUtil.btnLaunch.clicked.connect(self.press_launch)

        # SHOW the UI
        self.wgUtil.show()



    #=======================================================================
    # PRESS
    def press_help(self):
        webbrowser.open('https://github.com/kalvinirawan/script_manager')

    def press_save(self):
        print ('Saved!')

    def press_launch(self):
        print ('Launch!')


#===============================================================================
# START
def os_launch():
    app = QtWidgets.QApplication(sys.argv)
    classVar = ScriptManager()
    app.exec_()


def dcc_launch():
    global main_widget
    main_widget = ScriptManager()

os_launch()