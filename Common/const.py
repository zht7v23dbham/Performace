#-*- coding: UTF-8 -*-
'''
Created on 2016年3月3日

@author: zuohaitao
'''
import os

workSpace = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

resPath = os.path.join(workSpace,"res")

logPath = os.path.join(workSpace,"logs")

jarFile = os.path.join(workSpace,"MakeGraph.jar")

#apk packageName
packageName = "com.coolqi.partner"

#app启动activity
lunchActivity = "com.coolqi.partner.module.home.SpkashActivity"