#-*- coding:utf-8 -*-
from mysql import connector
import os
import time
import datetime
import mysql


class MySQL(object):
    """
    使用方法：

    >>> with MySQL('xvirt') as db:
    >>>     sql = 'select * from instances;'
    >>>     db.execute(sql)
    >>>     for a in db:
    >>>         print a
    """

    def __init__(self, database):
        self.conn = connector.connect(user='root', database=database)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor
    def commit(self):
        self.conn.commit()

    def __exit__(self, *exc):
        self.cursor.close()
        self.conn.close()

config={'host':'30.30.32.5',#连接的数据库IP地址 
'user':'root', 
'password':'0rd1230ac', 
'port':3306 ,#默认3306或31900 
'database':'v8_web', 
'charset':'utf8'#默认即为utf8 
} 
def init_db(timenode):
    timedailyp=time.strptime(timenode,"%Y-%m-%d %H:%M:%S")
    timedaily=time.strftime("%Y-%m-%d 00:00:00",timedailyp)
    with MySQL('v8_web') as db:
        sql = "insert into _cronsum_runlog (cron_name,data_start_time,data_end_time,mode,ctime) values ('cloudstatsum','%s','%s','daily','%s')"%(timedaily,timedaily,timedaily)
        db.execute(sql)
        db.execute('commit')
        sql = "delete from cloud_stat_daily"
        db.execute(sql)
        sql = "delete from _cronsum_runlog where cron_name='cloudstatsum' and mode='daily'"
        db.execute(sql)

def get_time(date):
    timenode=''
    with MySQL('v8_web') as db:
        sql="select timenode,sum(service) as service_sum from v8_web._cronsum_traffic_stat where date_format(timenode,'%%Y-%%m-%%d')='%s' group by timenode order by service_sum desc limit 1;"%date
        db.execute(sql)
        for result in db:
            timenode=result    
    return timenode


def get_metric(timenode):
    sql="select * from cloud_stat_minutely where make_time='%s'"%timenode
    db.execute(sql)
    metrics=[]
    for cloudtf in db:
        metrics.append(cloudtf)
    return metrics

def insert_metric(metrics):
    with MySQL('v8_web') as db:
        for metric in metrics:
            timedaily=metric[1].strftime("%Y-%m-%d 00:00:00")
            #create_time=(metric[1]+datetime.timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")
            sql="insert into cloud_stat_daily (make_time,direction,server,service_size,service,fsn,sn) values ('%s','%d','%s','%d','%d','%s','%s')"%(timedaily,metric[2],metric[3],metric[4],metric[5],metric[6],metric[7])
            db.execute(sql)
            db.execute('commit')

if __name__ == '__main__':
    timenode='2017-09-13 00:00:00'
    init_db(timenode)
    date=''
    today=time.strftime("%Y-%m-%d")
    results=[]
    while (date != today):
        timenode=datetime.datetime.strptime(timenode,"%Y-%m-%d %H:%M:%S")
        date=timenode.replace(hour=0, minute=0,second=0).strftime("%Y-%m-%d")
        result=get_time(date)
        if result != '':
            results.append(result)
        timenode=(timenode+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    print results
    with MySQL('v8_web') as db:
        for timenode in results:
            timenode=timenode[0].strftime("%Y-%m-%d %H:%M:%S")
            metrics=get_metric(timenode)
            insert_metric(metrics)
