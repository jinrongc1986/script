#-*- coding:utf-8 -*-
import subprocess
import os
import time
while True:
	times=raw_input("输入请求次数:\n")
	if times.isdigit():
		break
	else:
		print '请输入整数' 
ISOTIMEFORMAT='%Y-%m-%d %X'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
total = int(times)
type=raw_input("请输入文件格式:\n")
print 'running...'
for i in range(total):
  cmd = "curl -o /dev/null http://192.168.1.203/xixi/1.%s"%type
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print time.strftime( ISOTIMEFORMAT, time.localtime() )
