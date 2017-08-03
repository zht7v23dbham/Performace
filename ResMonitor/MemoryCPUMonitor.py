#-*- coding: UTF-8 -*-
'''
Created on 2016年2月25日

@author: zhujianpeng
'''
import threading
import os
import time
import subprocess
import sys
import signal
import re
from Common import const

class memoryCPUMonitor(threading.Thread):
    over = False

    def __init__(self,logFolder,caseID=None,deviceID=None,packageName=const.packageName):
        threading.Thread.__init__(self)
        self.over = False
        self.package = packageName
        self.logFolder = logFolder
        
        if caseID is None:
            self.picPre = "Test"
            self.logFile = os.path.join(self.logFolder,"memory.log")
        else:
            self.picPre = caseID
            self.logFile = os.path.join(self.logFolder,"%s_memory.log"%caseID)
        #每隔1秒取一次值
        if deviceID is None:
            self.cmdStr = 'adb shell "top -d 1 -s cpu | grep %s" > "%s"'%(self.package,self.logFile )#间隔1秒获取一次
        else:
            self.cmdStr = 'adb -s %s shell "top -d 1 -s cpu | grep %s" > "%s"'%(deviceID,self.package,self.logFile)
            
        self.over = False
#         print self.cmdStr
        
    @staticmethod
    def terminate():
        memoryCPUMonitor.over = True
        
        
    def run(self):
        "开始执行"
        print "CPU/Memory监控启动...".decode("utf-8")
        print self.cmdStr
        sub_process = subprocess.Popen(self.cmdStr,shell=True)
        memoryCPUMonitor.over = False
        while not memoryCPUMonitor.over:
            time.sleep(1)
            
        else:
            time.sleep(10)
            print "数据收集结束。".decode("utf-8")
            os.system("taskkill /F /IM adb.exe")
        time.sleep(2)
#         print "解析数据，制作图表。"
        print 'java -jar '+const.jarFile+' '+self.logFile+' '+self.picPre+' '+self.logFolder+' 0'
        #处理文件路径中带空格的情况
        if " " in const.jarFile:
            cmdStr = 'java -jar "'+const.jarFile+'" "'+self.logFile+'" '+self.picPre+' "'+self.logFolder+'" 0'
        else:
            cmdStr = 'java -jar '+const.jarFile+' '+self.logFile+' '+self.picPre+' '+self.logFolder+' 0'
        if sys.platform.startswith("win"):
            subprocess.call(cmdStr)
        elif sys.platform.startswith('linux'):
            subprocess.call(cmdStr,shell=True)
        print "制图完毕。".decode("utf-8")
            

            
if __name__ == "__main__":
#     p = parse()
#     p.parseLog("D:/test/cpu.log")
#     filePath = "D:/test/cpu.log"
#     picPath = "D:/test/graph/"
#     jarFile = "D:/eclipse/workspace/MakingGraph/MakeGraph.jar"
#     info = subprocess.call('java -jar '+jarFile+' '+filePath+' Case001 '+picPath)
#     logFolder = "D:/test/123/"
# #     caseID = ""
#     t = memoryCPUMonitor(logFolder)
#     t.start()
#     time.sleep(20)
#      
#     memoryCPUMonitor.terminate(True)
    print "over"
#     print const.jarFile
    