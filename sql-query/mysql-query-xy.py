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
conn = MySQLdb.Connection(host="192.168.1.225", user="selecter", passwd="fxdata_Select-2016", charset="UTF8")
conn.select_db('cds_v2')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 执行SQL
for i in range(25,26):
	m=str(i)
   	n=str(i+1)
   	s=m.zfill(2)
   	t=n.zfill(2)
   	sql=("SELECT * FROM (SELECT `make_time` - `make_time` %% (500) AS `newtime`, sum(per1sum) / 300 * 8 AS `per5avg` FROM (SELECT make_time,sum(proxy_cache_size) AS proxy_cache_sizes,sum(service_size) AS service_sizes,sum(service_size)-sum(proxy_cache_size) as per1sum FROM `cds_v2`.`operation_stat` WHERE  make_time >= '2016-12-%s 00:00:00' AND make_time < '2016-12-%s 00:00:00' AND sn like '%%A%%' AND sn not like '%%0530000196' AND sn not like '%%0530000152' AND category = 152 group by make_time) AS `a` GROUP BY `make_time` - `make_time` %% (500) ) AS `b` ORDER BY per5avg limit 1;")%(s,t)
	cursor.execute(sql)
	result=cursor.fetchall()
	print result
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()
