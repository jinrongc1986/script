#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import MySQLdb


# 连接数据库
conn = MySQLdb.Connection(host="192.168.1.12", user="selector", passwd="fxdata_Select-2016", charset="UTF8")
conn.select_db('ordoac')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

sql="select rhelp from feedback where sn='CAS0510000147'"
cursor.execute(sql)
rhelp_port=cursor.fetchall()
print rhelp_port


# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()