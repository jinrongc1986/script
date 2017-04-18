#-*- coding:utf-8 -*-
import subprocess
import os
import time
while True:
        start=raw_input("输入请求次数:\n")
        if start.isdigit():
                break
        else:
                print '请输入整数'
while True:
        stop=raw_input("输入请求次数:\n")
        if stop.isdigit():
                break
        else:
                print '请输入整数'
ISOTIMEFORMAT='%Y-%m-%d %X'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
#type=raw_input("请输入文件格式:\n")
start=int(start)
stop=int(stop)
print 'running...'
for i in range(start,stop+1):
        cmd = "curl -o /dev/null 'http://20.20.20.4/test/%d.flv'"%i
#	print cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print time.strftime( ISOTIMEFORMAT, time.localtime() )
