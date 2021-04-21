#!/usr/bin/python

from PySide import QtGui
import sys
import windows
from vars import * 



class MainWindow(QtGui.QMainWindow):

    def __init__(self, titile, pos_x, pos_y, \
                width=DEFAULT_M_WINDOW_WIDTH, hight=DEFAULT_M_WINDOW_HIGHT):
        super(MainWindow, self).__init__()

        self.__title = titile
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__hight = hight

        self.initUI()
        self.createMenu()


    def initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.setWindowTitle(self.__title)



    def createMenu(self):
        
        self.__action_edit_conf     = QtGui.QAction("edit config", self)
        self.__action_run_scripts   = QtGui.QAction("run scripts", self)


        self.__action_edit_conf.triggered.connect(self.edit_conf)
        self.__action_run_scripts.triggered.connect(self.run_scripts)

        
        self.__menubar              = self.menuBar()


        self.__edit_conf            = self.__menubar.addMenu("edit")
        self.__run_scripts          = self.__menubar.addMenu("run")


        self.__edit_conf.addAction(self.__action_edit_conf)
        self.__run_scripts.addAction(self.__action_run_scripts)



    def edit_conf(self):
        pass


    def run_scripts(self):
        pass



    def show_window(self):
        self.show()



def main():
    app = QtGui.QApplication(sys.argv)
    
    mWindow = MainWindow(
        MAIN_WINDOW_TITLE,
        DEFAULT_M_WINDOW_POS_X, 
        DEFAULT_M_WINDOW_POS_Y
    )

    mWindow.show_window() 
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()