#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys
import MySQLdb
import time

# 设置默认编码为UTF-8，否则从数据库
# 读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接数据库
conn = MySQLdb.Connection(host="localhost", user="root", passwd="", charset="UTF8")
conn.select_db('cache')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 执行SQL
tables=['http_cache','mobile_cache','video_cache']
hosts=['m9.music.126.net','img.samsungapps.com','dl.cm.sec.miui.com','download.gfe.nvidia.com']
time
for tuple2 in tuple1:
    grade=tuple2[0]
    clas=tuple2[1]
    catestart=tuple2[2]
    cateend=tuple2[3]
    for category in range(catestart,cateend+1):
        sql="insert into ftop_http_get_stat_day values ('2016-12-14 00:00:00',%d,%d,%d,%d,50,'CAS0510000127')"%(grade,clas,category,num)
	cursor.execute(sql)
	num=num+1
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()
