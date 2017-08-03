#-*- coding: UTF-8 -*-
'''
Created on 2016年2月23日

@author: zhujianpeng
'''
import threading
import os
from Common import const

class powerMonitor(threading.Thread):
    over = False
    
    def __init__(self,logFolder,deviceNo=None,packageName=const.packageName):
        threading.Thread.__init__(self)
        self.packageName = packageName
        self.deviceNo = deviceNo
        self.over = False
        
    @staticmethod
    def terminate():
        powerMonitor.over = True
        
    def getCurrentBattery(self):
        "获取当前手机的电量"
        if self.deviceNo:
            cmdStr = 'adb -s %s shell "dumpsys battery | grep level"' % (self.deviceNo)
        else:
            cmdStr = 'adb shell "dumpsys battery | grep level"'
            
        current_battery = os.popen(cmdStr).read().split(": ")[1]
        return current_battery
    def run(self):
        "执行监控"
        print "电量监控启动...".decode("utf-8")
        while not powerMonitor.over:
            print "kkk"
        
if __name__ == "__main__":
    p = powerMonitor("353BCJMKJEF3")
    print p.getCurrentBattery()    