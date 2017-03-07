#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys
import MySQLdb
import getopt
opts,arts = getopt.getopt(sys.argv[1:],"hi:cd")
init=1
for op,value in opts:
	if op=="-i":
		ipstart=value
	elif op=="-c":
		init=1
	elif op=='-d':
		init=0
	elif op=="-h":
		print "-c:创建 -d:删除"
		sys.exit()

# 设置默认编码为UTF-8，否则从数据库
# 读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接数据库
conn = MySQLdb.Connection(host="30.30.32.3", user="root", passwd="0rd1230ac", charset="UTF8")
conn.select_db('datap2c')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 执行SQL
x=1
y=10001
for hours in range(11,16):
	for mintues in range (11,50):
		ctimed='2017-03-02 %d:%d:00'%(hours,mintues)
		named='xvirt_traffic_stat'
		mtimed='2017-03-02 %d:%d:00'%(hours,mintues-1)
		datad="('%s',%d,%d,'CAS0510000127')" % (mtimed,x,y)
		if init==1:
			sql="""insert into data (create_time,name,format,status,make_time,datanum,datasize,data) values ('%s','%s',0,0,'%s',2,50,"%s")"""%(ctimed,named,mtimed,datad)
		else :
			sql="""delete from data where create_time='%s' and name='%s' and make_time ='%s'"""%(ctimed,named,mtimed)
			print sql
		cursor.execute(sql)
		x+=1
		y+=1
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()
