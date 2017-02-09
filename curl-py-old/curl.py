#!/usr/bin/python
#-*- coding:utf-8 -*-
import subprocess
import os
import time
import sys
import getopt
opts,arts = getopt.getopt(sys.argv[1:],"hn:u:")
while True:
	times=raw_input("输入请求次数:\n")
	if times.isdigit():
		break
	else:
		print '请输入整数' 
ISOTIMEFORMAT='%Y-%m-%d %X'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
total = int(times)
#type=raw_input("请输入文件格式:\n")
print 'running...'
for i in range(total):
  cmd = "curl --head http://kascdn.kascend.com/jellyfish/uiupload/images/roombillboard/right_img.png"
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print time.strftime( ISOTIMEFORMAT, time.localtime() )
