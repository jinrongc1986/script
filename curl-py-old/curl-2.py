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
#type=raw_input("请输入文件格式:\n")
print 'running...'
oksum=0
noksum=0
for i in range(total):
  	cmd = "curl --head 'http://mvimg2.meitudata.com/587ef39ed39d97091.jpg'"
  	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output1=str(p.communicate())
	# print type(output1)
	url = output1.split(' ')[-4]
	if url == 'http://30.30.32.3/cache/1/04/meitudata.com/c61d84052342816d393a8c8b9df47095/587ef39ed39d97091.jpg\\r\\nContent-Length:':
		print 'OK'
		oksum+=1
	else:
		print  url
		noksum+=1
print "ok:%d,nok:%d,ok/nok:%0.2f"%(oksum,noksum,oksum/(oksum+noksum))
print time.strftime( ISOTIMEFORMAT, time.localtime() )
