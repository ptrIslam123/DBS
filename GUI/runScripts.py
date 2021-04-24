#!/usr/bin/python

import os



def runExecTasks():
    os.system("cd ../emailService/; python main.py -he")
    

def getNetSettingAndRunTasks(emailAddr, password):
    cmd = "cd ../emailService/; python main.py -ne " + emailAddr + " " + password
    os.system(cmd)