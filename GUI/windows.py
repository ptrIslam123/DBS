#!/usr/bin/python

from PySide import QtGui
from vars import *
import json

class BaseWindow(QtGui.QWidget, object):

    def __init__(self, titile, pos_x, pos_y, width=300, hight=300):
        super(BaseWindow, self).__init__()

        self.__title = titile
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__hight = hight

        self.initUI()


    def initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.setWindowTitle(self.__title)



    def show_window(self):
        self.show()


    def close_window(self):
        print("close this window!")

    

class WindowEditConf(BaseWindow):
    
    def __init__(self, titile, pos_x, pos_y, \
            width=DEFAULT_M_WINDOW_WIDTH, hight=DEFAULT_M_WINDOW_HIGHT):
        super(WindowEditConf, self).__init__(titile, pos_x, pos_y, width, hight)
        
        self.__resultFileName   = None
        self.__emailTo          = None
        self.__scripts          = None
        self.__password         = None
        self.__dataFileName     = None
        self.__emailFrom        = None

        self.createEditDialog()


    def createEditDialog(self):
        self.__gridBox  = QtGui.QGridLayout()

        self.__reconf   = QtGui.QPushButton("reconfigure")

        resultFileNameLabel = QtGui.QLabel("result file name")
        emailToLabel        = QtGui.QLabel("email to")
        scriptsLabel        = QtGui.QLabel("scripts")
        passwordLabel       = QtGui.QLabel("password")
        dataFileNameLabel   = QtGui.QLabel("target file name")
        emailFromLabel      = QtGui.QLabel("emaill from")


        self.__resultFileNameLineEdit   = QtGui.QLineEdit()
        self.__emaillToLineEdit         = QtGui.QLineEdit()
        self.__scriptsLineEdit          = QtGui.QLineEdit()
        self.__passwordLineEdit         = QtGui.QLineEdit()
        self.__dataFileNameLineEdit     = QtGui.QLineEdit()
        self.__emailFromLineEdit        = QtGui.QLineEdit()


        self.__gridBox.addWidget(resultFileNameLabel, 1, 1)
        self.__gridBox.addWidget(emailToLabel, 2, 1)
        self.__gridBox.addWidget(scriptsLabel, 3, 1)
        self.__gridBox.addWidget(passwordLabel, 4, 1)
        self.__gridBox.addWidget(dataFileNameLabel, 5, 1)
        self.__gridBox.addWidget(emailFromLabel, 6, 1)


        self.__gridBox.addWidget(self.__resultFileNameLineEdit, 1, 2)
        self.__gridBox.addWidget(self.__emaillToLineEdit, 2, 2)
        self.__gridBox.addWidget(self.__scriptsLineEdit, 3, 2)
        self.__gridBox.addWidget(self.__passwordLineEdit, 4, 2)
        self.__gridBox.addWidget(self.__dataFileNameLineEdit, 5, 2)
        self.__gridBox.addWidget(self.__emailFromLineEdit, 6, 2)
        self.__gridBox.addWidget(self.__reconf, 7, 2)


        self.setLayout(self.__gridBox)


        self.__reconf.clicked.connect(self.reconfigure)



    def reconfigure(self):
        self.__resultFileName   = self.__resultFileNameLineEdit.text()
        self.__emailTo          = self.__emaillToLineEdit.text()
        self.__scripts          = self.__scriptsLineEdit.text()
        self.__password         = self.__passwordLineEdit.text()
        self.__dataFileName     = self.__dataFileNameLineEdit.text()
        self.__emailFrom        = self.__emailFromLineEdit.text()

       
        self.makeJsonDict(
            self.__resultFileName,
            self.__emailTo,
            self.__scripts,
            self.__password,
            self.__dataFileName,
            self.__emailFrom
        )

        self.writeJsonDictToFile(MAIN_CONFIG_PATH_FILE, self.__jsonDicrt)
        self.close_window()

    def writeJsonDictToFile(self, fname, jsonObj):
        with open(fname, 'w') as file:
            json.dump(jsonObj, file, indent=4)


    def readJsonFromFile(self, fname):
        pass



    def makeJsonDict(self, result_fn, email_to, scripts, password, \
                                                data_fn, email_from):
         
         scripts_list = scripts.split(',')
         
         self.__jsonDicrt = {
            "result_fname": result_fn, 
            "email_to": email_to, 
            "scripts": scripts_list, 
            "password": password, 
            "data_fname": data_fn, 
            "email_from": email_from
        }

        

    def get_result_file_name(self):
        return self.__resultFileName


    def get_email_to(self):
        return self.__emailTo


    def get_scripts(self):
        return self.__scripts


    def get_password(self):
        return self.__password


    def get_data_file_name(self):
        return self.__dataFileName


    def get_email_from(self):
        return self.__emailFrom





class WindowNetSettings(BaseWindow):

    def __init__(self, titile, pos_x, pos_y, \
            width=DEFAULT_M_WINDOW_WIDTH, hight=DEFAULT_M_WINDOW_HIGHT):
        super(WindowNetSettings, self).__init__(titile, pos_x, pos_y, width, hight)
        
        self.__email_addr   = None
        self.__password     = None

        self.createNetSettingsDialog()


    def createNetSettingsDialog(self):
        self.__gridBox  = QtGui.QGridLayout()

        self.__applyBtn = QtGui.QPushButton("apply")

        emailAddrLabel  = QtGui.QLabel("email address")
        passwordLabel   = QtGui.QLabel("password")

        self.__emailAddrLineEdit = QtGui.QLineEdit()
        self.__passwordLineEdit = QtGui.QLineEdit()


        self.__gridBox.addWidget(emailAddrLabel, 1, 1)
        self.__gridBox.addWidget(passwordLabel, 2, 1)
        self.__gridBox.addWidget(self.__emailAddrLineEdit, 1, 2)
        self.__gridBox.addWidget(self.__passwordLineEdit, 2, 2)
        self.__gridBox.addWidget(self.__applyBtn, 3, 2)

        self.setLayout(self.__gridBox)

        self.__applyBtn.clicked.connect(self.applyConf)


    def applyConf(self):
        self.__email_addr   = self.__emailAddrLineEdit.text()
        self.__password     = self.__passwordLineEdit.text()
        self.close_window()
        


    def get_email_addr(self):
        return self.__email_addr


    def get_password(self):
        return self.__password
        