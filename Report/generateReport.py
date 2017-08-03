# -* - coding: UTF-8 -* - 

import os
from Report import reportWritor
import time
from ResMonitor.NetworkTraffic import networkTraffic


report_dir = os.path.join(os.path.dirname(__file__), 'results') 
report_dir = "D:/eclipse/workspace/MobilePerformance/logs/task_0304113023"

def formatStr1(d):
    "{'duration': 2, 'crashCount': '0', 'anrCount': '0', 'pkgName': 'cn.com.gome.coolqi', 'deviceID': 'HC52SWME0349'}"
    
    s = "此次测试时长%d分钟，测试设备ID【%s】,其中crash数量%d个，ANR数量%d个。"%(d["duration"],d["deviceID"],int(d['crashCount']),int(d['anrCount']))
    return s

def formatStr2(d):
    "{'count': 10, 'max': 2369ms, 'avg': 1929ms, 'min': 1802ms}"
    s = "此次测试共执行%d次，其中最大时间为 %d ms，最小时间为 %d ms,平均时间为 %d ms"%(d['count'],int(d['max']),int(d['min']),int(d['avg']))
    return s

def generateReportEx(resultDict,report_dir):
    "生成报告"
    "resultList-测试结果数据"
    
#     resultDict = {'testItems': {'startTime': {'count': 3, 'max': 1877L, 'avg': 1839L, 'min': 1781L}}, 'endTime': '2016/03/04 14:42:27', 'startTime': '2016/03/04 14:42:11'}
    start_time = resultDict["startTime"]
    end_time = resultDict["endTime"]
    use_time = resultDict["useTime"]
    monkeyResult = None
    startTimeResult = None
    
    if resultDict["testItems"].has_key("monkeyTest"):
        monkeyResult = resultDict["testItems"]["monkeyTest"]
    if resultDict["testItems"].has_key("startTime"):
        startTimeResult = resultDict["testItems"]["startTime"]
    
    testItemStr = "测试内容包括："
    if len(resultDict["testItems"]) == 0:
        testItemStr += "手工操作。"
    else:
        testItemStr += "，".join(resultDict["testItems"].keys())
        testItemStr = testItemStr.replace("monkeyTest", "monkey测试")
        testItemStr = testItemStr.replace("startTime", "启动时间测试")
    
    
    report = reportWritor.Report(report_dir)
    
#     report.write_line("<h1>美信自动化 测试报告</h1>")
    
    #测试结果总结部分--begin
    report.write_line('<div>')
    report.write_line('<p>Hi,all:<br><br>本次测试完成，测试开始时间：%s，结束时间：%s，共计：%s秒。%s。</p>'%(start_time,end_time,use_time,testItemStr))
    report.write_line('</div>')
    #测试结果总结部分--end
    
    #测试结果详细部分--begin
    
    #Monkey测试部分
    if monkeyResult is not None:
        report.write_line('<div>')
        report.write_line('<p>Monkey测试结果:<br>%s</p>'%formatStr1(monkeyResult))
        report.write_line('</div>')
    #启动时间部分
    if startTimeResult is not None:
        report.write_line('<div>')
        report.write_line('<p>启动时间测试结果:<br>%s</p>'%formatStr2(startTimeResult))
        report.write_line('</div>')
    #资源图表
    print os.path.join(report_dir,"Test_cpuInfo.png")
    if os.path.exists(os.path.join(report_dir,"Test_cpuInfo.png")):
        
        report.write_line('<div>')
        report.write_line('<h4>CPU使用统计（%）：</h4>')
        report.write_line('<img src="Test_cpuInfo.png" width="900"></img>')
        report.write_line('</div>')
    
    if os.path.exists(os.path.join(report_dir,"Test_MemoryInfo.png")):
        report.write_line('<div>')
        report.write_line('<h4>内存使用统计（MB/s）：</h4>')
        report.write_line('<img src="Test_MemoryInfo.png" width="900"></img>')
        report.write_line('</div>')
    
    if os.path.exists(os.path.join(report_dir,"Test_networkTraffic.png")):
        report.write_line('<div>')
        report.write_line('<h4>流量使用统计（KB/s）：</h4>')
        report.write_line('<h4>本次测试的总流量为（KB）：'+str(round((networkTraffic.total_bytes/1024.0),2))+'KB</h4>')
        report.write_line('<img src="Test_networkTraffic.png" width="900"></img>')
        report.write_line('</div>')
    
    if os.path.exists(os.path.join(report_dir,"Test_powerInfo.png")):
        report.write_line('<div>')
        report.write_line('<h4>电量使用统计（%）：</h4>')
        report.write_line('<img src="Test_cpuInfo.png" width="900"></img>')
        report.write_line('</div>')
    #测试结果详细部分--end
    
    report.write_closing_html()
    print "报告生成完毕。".decode("utf-8")
    return report.fn

def getReportConent(fileName=None):
    if fileName is not None:
        reportFile = os.path.join(report_dir,fileName)
        return open(reportFile).read()
    return None
    
    
if __name__ == "__main__":
#     startTime = time.strftime("%Y/%m/%d %H:%M:%S")
#     time.sleep(3)
#     endTime = time.strftime("%Y/%m/%d %H:%M:%S")
    path = "D:/eclipse/workspace/MobilePerformance/logs/task_0304150853"
#     resultDict = {"startTime":startTime,"endTime":endTime,"testItems":{"monkeyTest":{"time":20,"crash":0},"startTime":{"avg":1209,"max":1388}}}
    rd = {'testItems': {'startTime': {'count': 3, 'max': 1877L, 'avg': 1839L, 'min': 1781L}}, 'endTime': '2016/03/04 14:42:27', 'startTime': '2016/03/04 14:42:11'}
    generateReportEx(rd,path)
    print "over"
    