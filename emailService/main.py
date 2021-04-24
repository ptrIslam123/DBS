#!/usr/bin/env python 
#-*-coding: utf-8-*-

import vars as env
import sendGmail as sGmail
import sendReport as sReport
import readGmail as rGmail
import parseConfSMTP as pConf
import execTasks as execT
import sysloger 
import sys
import os


def createWorkFile(wordData):
    pConf.writef(env.MAIN_DATA_FILE_PATH, wordData)
    sysloger.log(env.EVENT_CREATE_WORD_SPACE)


def clearWordSpace(fname):
    pConf.removef(fname)
    sysloger.log(env.EVENT_CLEAR_WORK_SPACE + fname)


def runTasks(task_list, data, result_fn):
    if not (isinstance(task_list, list)):
        return -1

    createWorkFile(data)

    for task in task_list:
        taskFileName = env.SCRIPTS_DIR_PATH + task

        if os.path.exists(taskFileName):
            execT.execTaskAndWriteResultToFile([taskFileName], result_fn)
            sysloger.log(env.EVENT_RUN_TASK + taskFileName)

        else:
            sysloger.log(env.ERROR_FILE_NOT_FOUND + taskFileName)


    



def sendReport():
    sReport.sendReport(env.MAIN_CONFIG_FILE_PATH)
    sysloger.log(env.EVENT_SEND_REPORT)


def sendData(email_from, email_to, password, data, fname):
    sGmail.sendGmail(email_from, email_to, env.DBS_DATA_SUBJECT_TYPE,\
                     password, data, fname)
    sysloger.log(env.EVENT_SEND_DATA)



def sendConfData(email_from, email_to, password, confData, confName):
    sGmail.sendGmail(email_from, email_to, env.DBS_CONF_SUBJECT_TYPE, \
                    password, confData, confName)
    sysloger.log(env.EVENT_SEND_CONF)




def getReport(email_addr, password):
    emailS = rGmail.readGmail(email_addr, password, \
                                 env.DBS_REPORT_SUBJECT_TYPE)

    sysloger.log(env.EVENT_GET_REPORT)
    return emailS



def getData(email_addr, password):
    emailS = rGmail.readGmail(email_addr, password, \
                            env.DBS_DATA_SUBJECT_TYPE)
    sysloger.log(env.EVENT_GET_DATA)
    return emailS.get_body()


def getConfData(email_addr, password):
    emailStruct = rGmail.readGmail(email_addr, password, \
                                env.DBS_CONF_SUBJECT_TYPE)
    jsonStruct = emailStruct.get_body()
    sysloger.log(env.EVENT_GET_CONF)
    return pConf.strToJsonConfStruct(jsonStruct)



def getSettingsFromNetAndExecuteTasks(email_addr, password):

    emailS      = getConfData(email_addr, password)
    targetData  = getData(email_addr, password)

    email_from  = emailS.get_email_from()
    email_to    = emailS.get_email_to()
    password    = emailS.get_password()

    task_list   = emailS.get_scripts()
    data_fn     = emailS.get_data_fname()
    result_fn   = emailS.get_result_fname()

    # execute set tasks! 
    runTasks(task_list, targetData, result_fn)


    # send report to email server!
    reportData = pConf.readf(env.REPORT_DIR_PATH + result_fn)

    sGmail.sendGmail(email_from, email_to, env.DBS_REPORT_SUBJECT_TYPE, \
                password, reportData, result_fn)

    clearWordSpace(env.REPORT_DIR_PATH + result_fn)


def executeTasks(jsonConf):    
    jsonStruct  = pConf.getConf(jsonConf)

    task_list   = jsonStruct.get_scripts()
    target_data = pConf.readf(env.MAIN_DATA_FILE_PATH)
    result_fn   = jsonStruct.get_result_fname()

    runTasks(task_list, target_data, result_fn)
    



def main():
    flag = sys.argv[1]
    
    if flag == "-he":
            # python main.py -he
            executeTasks(env.MAIN_CONFIG_FILE_PATH)

    elif flag == "-ne":
        # python main.py -ne email_addr password
        email_addr, password = sys.argv[2], sys.argv[3]
        getSettingsFromNetAndExecuteTasks(email_addr, password)

    else:
        sysloger.log(env.INVALID_START_PARAM + flag)
        sys.exit(-1)





if __name__ == "__main__":
    main()