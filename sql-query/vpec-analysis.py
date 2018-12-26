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
conn = MySQLdb.Connection(host="192.168.2.17", user="root", passwd="0rd1230ac",
                          charset="UTF8")
conn.select_db('vpec')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 执行SQL
sql = """ select sn,avg(all_ip),avg(http_ip),avg(demand_ip),avg(live_ip) from ip_service where   all_ip>1000 and http_ip>1000 and demand_ip>1000 and live_ip>1000 group by sn"""
cursor.execute(sql)
result = cursor.fetchall()
print result
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()
