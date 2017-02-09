#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys
import MySQLdb
import getopt
opts,arts = getopt.getopt(sys.argv[1:],"hi:t:H:M:c:")
ipstart="10.10.10.1"
logtype="video"
hour=1
minute=0
catestart=0
cateend=21
for op,value in opts:
	if op=="-i":
		ipstart=value
	elif op=="-t":
		logtype=value
	elif op=="-H":
		hour=value
	elif op=="-M":
		minute=value
		minute=int(minute)
	elif op=="-c":
		cateend=value
		cateend=int(cateend)
	elif op=="-h":
		print "支持IP,-i;\n支持video,http,mobile类型选择,-t"
		sys.exit()
if logtype=="video":
	logfile='video_service_log'
elif logtype=="mobile":
	logfile="mobile_service_log"
elif logtype=="http":
	logfile="http_service_log"

# 设置默认编码为UTF-8，否则从数据库
# 读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接数据库
conn = MySQLdb.Connection(host="localhost", user="root", passwd="", charset="UTF8")
conn.select_db('cache')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 计算起始IP
if not ipstart=="":
	ip123=ipstart.split('.')[0]+'.'+ipstart.split('.')[1]+'.'+ipstart.split('.')[2]+'.'
	ip4=int(ipstart.split('.')[3])
	#print ip123
	#print ip4
# 执行SQL
if logtype=="mobile":
	for category in range(catestart,cateend+1):
		minute=minute+1
		minute1=str(minute).zfill(2)
		hour1=str(hour).zfill(2)
		filename='test'+minute1
        	sql="insert into %s values ('2017-02-07 %s:%s:00','%s%d','038c18a73f7c55c93b444e5439ed4288','',%d,'haha.com','%s',20000000,20000000,60000,'30.30.32.3',0,'windows')"%(logfile,hour1,minute1,ip123,ip4,category,filename)
		ip4=ip4+1
		cursor.execute(sql)
else :
	for category in range(catestart,cateend+1):
                minute=minute+1
                minute1=str(minute).zfill(2)
                hour1=str(hour).zfill(2)
                filename='test'+minute1
                sql="insert into %s values ('2017-02-07 %s:%s:00','%s%d','038c18a73f7c55c93b444e5439ed4288','',%d,'haha.com','%s',20000000,20000000,60000,'30.30.32.3','windows')"%(logfile,hour1,minute1,ip123,ip4,category,filename)
                ip4=ip4+1
                cursor.execute(sql)
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()
