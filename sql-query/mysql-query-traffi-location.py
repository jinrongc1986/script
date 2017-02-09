#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys
import MySQLdb

# 设置默认编码为UTF-8，否则从数据库
# 读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接数据库
conn = MySQLdb.Connection(host="", user="root", passwd="", charset="UTF8")
conn.select_db('cache')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 执行SQL
for i in range(1,31):
	m=str(i)
   	n=str(i+1)
   	s=m.zfill(2)
   	t=n.zfill(2)
	sql1=("select timenode,counts,sums from ( select date_format(create_time,'%%Y-%%m-%%d') as timenode,count(*) as counts from location_log where create_time >='2016-12-%s 00:00:00' and create_time <'2016-12-%s 00:00:00')as s left join (select date_format(ctime,'%%Y-%%m-%%d') as timenode1,sum(service_size) as sums from operation_stat where ctime >='2016-12-%s 00:00:00' and ctime <'2016-12-%s 00:00:00') as t on s.timenode=t.timenode1;")%(s,t,s,t)
	cursor.execute(sql1)
	result=cursor.fetchall()
	print result
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()
