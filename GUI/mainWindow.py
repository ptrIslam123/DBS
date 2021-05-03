#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import sys
import windows
import runScripts
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

        self.__editConfWindow       = None
        self.__netSettingsWindow    = None
        
        self.initUI()
        self.createMenu()


    def initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.__textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.__textEdit)

        self.setWindowTitle(self.__title)



    def createMenu(self):
        
        self.__action_open_file     = QtGui.QAction("open file", self)
        self.__action_close_file    = QtGui.QAction("close file", self)
        self.__action_save_file     = QtGui.QAction("save file as", self)
        self.__action_close_app     = QtGui.QAction("Exit", self)
        self.__action_edit_conf     = QtGui.QAction("edit config", self)
        self.__action_run_scripts   = QtGui.QAction("run this current configure", self)
        self.__action_set_font      = QtGui.QAction("font", self)
        self.__action_get_settings_and_run_scripts = QtGui.QAction("get settings and run", self) 

        self.__action_edit_conf.triggered.connect(self.edit_conf)
        self.__action_run_scripts.triggered.connect(self.run_scripts)
        self.__action_get_settings_and_run_scripts.triggered.connect(self.get_settings_and_run_scripts)
        self.__action_open_file.triggered.connect(self.read_file)
        self.__action_close_file.triggered.connect(self.close_file)
        self.__action_save_file.triggered.connect(self.save_file)
        self.__action_close_app.triggered.connect(self.close_window)
        self.__action_set_font.triggered.connect(self.set_font)

        
        self.__menubar              = self.menuBar()


        self.__file                 = self.__menubar.addMenu("File") 
        self.__edit_conf            = self.__menubar.addMenu("Edit")
        self.__view                 = self.__menubar.addMenu("View")
        self.__run_scripts          = self.__menubar.addMenu("Run")


        self.__file.addAction(self.__action_open_file)
        self.__file.addAction(self.__action_close_file)
        self.__file.addAction(self.__action_save_file)
        self.__file.addAction(self.__action_close_app)
        self.__edit_conf.addAction(self.__action_edit_conf)
        self.__view.addAction(self.__action_set_font)
        self.__run_scripts.addAction(self.__action_run_scripts)
        self.__run_scripts.addAction(self.__action_get_settings_and_run_scripts)
        



    def edit_conf(self):
        if self.__editConfWindow is None:
            self.__editConfWindow = windows.WindowEditConf("the edit window", 300, 300)
        
        self.__editConfWindow.show_window()


    def run_scripts(self):
        runScripts.runExecTasks()


    def get_settings_and_run_scripts(self):
        if self.__netSettingsWindow is None:
            self.__netSettingsWindow = windows.WindowNetSettings("the net settings window", 300, 300)

        self.__netSettingsWindow.show_window()



    def read_file(self):
        fname = self.getWorkFileName()

        with open(fname, 'r') as file:
                text = file.read().decode("utf-8")
                self.__textEdit.setText(text)
        


    def close_file(self):
        self.__textEdit.setText("")



    def save_file(self):
        text    = self.__textEdit.toPlainText()
        fname   = self.getWorkFileName()

        with open(fname, 'w') as file:
            file.write(text)
        


    def getWorkFileName(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '../config/reports')
        return fname
    

    def set_font(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.__textEdit.setFont(font)


    def show_window(self):
        self.show()

    
    def close_window(self):
        QtCore.QCoreApplication.instance().quit()


       


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