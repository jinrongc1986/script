#-*- coding:utf-8 -*-
import subprocess,urllib2
import os,sys
import time
from threading import Thread
import getopt


opts,arts = getopt.getopt(sys.argv[1:],"hu:n:")
url=""
total=1
for op,value in opts:
        if op=="-u":
                url=value
        elif op=="-n":
                total=value
		total=int(total)
def open_website(url):
	try:
		return urllib2.urlopen(url)
	except urllib2.HTTPError:
		pass
#while True:
#	times=raw_input("输入请求次数:\n")
#	if times.isdigit():
#		break
#	else:
#		print '请输入整数' 
ISOTIMEFORMAT='%Y-%m-%d %X'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
#total = int(times)
#type=raw_input("请输入文件格式:\n")
print 'running...'
if url=="":
	for i in range (0,total):
		Thread(target=open_website,args=["http://20.20.20.2/cache/9/8d/qq.com/1c2de58017fb39f0b01047b0de374344/b1644rmdie0.mp4?sdtfrom=v1099&type=mp4&vkey=CEB988C55ECBA00A060E8C27E4DEA0282333E76699946E58E0B1002D32690BA8B45DC52E9A05A881AF1F59D4D33833BBB5DAC47ADE10611318C31231E8CB62F2EBAEA2F97FF30A9937B0E53338268106F7CBD23D54B6420B&level=0&platform=3060202&br=64&fmt=mp4&sp=0&guid=36F6277ADE1E75EDFBBA76931076047243F72979"]).start()

else :
	for i in range (0,total):
		Thread(target=open_website,args=[url]).start()
'''
oksum=0
noksum=0
for i in range(total):
  	request=urllib2.Request('http://mvimg2.meitudata.com/587ef39ed39d97091.jpg')
	request.get_method=lambda:'HEAD'
	response=urllib2.urlopen(request)
	if response.geturl()== 'http://30.30.32.3/cache/1/04/meitudata.com/c61d84052342816d393a8c8b9df47095/587ef39ed39d97091.jpg':
		print 'OK'
		oksum+=1
	else:
		print  response.geturl()
		noksum+=1
	time.sleep(10)
print "ok:%d,nok:%d,ok/nok:%0.2f"%(oksum,noksum,oksum/(oksum+noksum))
'''
print 'finished'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
