# -*- coding: utf-8 -*-

import sys
import MySQLdb

sn=sys.argv[1]
def get_cds_info(sn='CAS0510000147'):
    # mysql -h 192.168.1.12 -uselector -pfxdata_Select-2016 -P 3305
    # 连接数据库
    conn = MySQLdb.Connection(host="192.168.1.12", user="selector", passwd="fxdata_Select-2016", charset="UTF8",port=3305)
    conn.select_db('ordoac')
    # 创建指针，并设置数据的返回模式为字典
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    sql="select rhelp from feedback where sn='%s'"%sn
    cursor.execute(sql)
    rhelp_port=cursor.fetchall()
    # 关闭指针
    cursor.close()
    # 关闭数据库连接
    conn.close()
    if rhelp_port:
        ssh_port=rhelp_port[0].get("rhelp").split(':')[2]
        f=open('rhelp.txt','w')
        f.write(ssh_port)
        f.close
        return "get ssh_port success"
    else :
        print "rhelp not exist"
        ssh_port=""
        f=open('rhelp.txt','w')
        f.write(ssh_port)
        f.close
        return "get ssh_port failed"

#if __name__=='__main__':
get_cds_info(sn)