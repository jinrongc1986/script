#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys,time
import MySQLdb
import getopt
import subprocess
import ssh
#命令行参数设置
opts,arts = getopt.getopt(sys.argv[1:],"hn:t:s:T:i:")
cachetype="video"
times=2
round_time=0
seconds=1
ipaddr='30.30.32.3'
for op,value in opts:
	if op=="-n":
		times=value
		times=int(times)
	elif op=="-t":
		cachetype=value
	elif op=="-i":
		ipaddr=value
	elif op=="-T":
		round_time=value
		round_time=int(round_time)
	elif op=="-s":
		seconds=value
		seconds=int(seconds)
	elif op=="-h":
		print "支持循环次数,默认2次: -n  X"
		print "支持video,http,mobile类型选择,默认video: -t XXX"
		print "支持每个curl间的等待时间选择，单位为秒，默认为1秒: -s x"
		sys.exit()
cachefile=cachetype + '_cache'
logfile  =cachetype + '_service_log'



# 设置默认编码为UTF-8，否则从数据库读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接数据库
conn = MySQLdb.Connection(host=ipaddr, user="root", passwd="0rd1230ac", charset="UTF8")
conn.select_db('cache')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

#检查icached capture uri数目
ssh_cmd_icached='/home/icache/icached debug'
ssh_result=ssh.main(ssh_cmd_icached)
cap_uri_str=int(ssh_result.split('capture uri:')[1].split("\n")[0].strip(" "))

#启动时间
ISOTIMEFORMAT='%Y-%m-%d %X'
print 'start curl at time:'
starttime=time.strftime( ISOTIMEFORMAT, time.localtime() )
print starttime

#执行curl动作
sql_query="select uri from "+cachefile
cursor.execute(sql_query)
results=cursor.fetchall()
print 'total uri is %d'%len(results)
for i in range(times):
	print 'round : %d'%(i+1) 
	print 'running...'
	for result in results:
		uri=result['uri']
		cmd="curl -o /dev/null -L '"+uri+"' --user-agent '"+str(i+1)+"'"
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		time.sleep(seconds)
	print 'round %d success'%(i+1)
	print 'wait for %d second'%round_time
	time.sleep(round_time)
# 准备执行结果比较
print 'stop curl & wait for result...'
time.sleep(10)
curl_num=times*len(results)

#检查icached capture uri最新数目,并计算curl期间的uri数量
ssh_cmd_icached='/home/icache/icached debug'
ssh_result=ssh.main(ssh_cmd_icached)
cap_uri_end=int(ssh_result.split('capture uri:')[1].split("\n")[0].strip(" "))
cap_uri_num=cap_uri_end-cap_uri_str

#获取数据库日志条目数并比对curl执行数量，已确认服务是否全部成功
sql_query_1="select count(*) from "+logfile+" where create_time > '%s';"%(starttime)
cursor.execute(sql_query_1)
log_results=cursor.fetchall()
log_num=int(log_results[0]['count(*)'])

sql_query_2="select count(*) from location_log where create_time > '%s' and client_ip='%s';"%(starttime,ipaddr)
cursor.execute(sql_query_2)
location_results=cursor.fetchall()
location_num=int(location_results[0]['count(*)'])

if log_num==curl_num:
	print 'all %d curls successfully!'%log_num
else :
	print 'The number of curls is %d'%curl_num
	print 'The number of captured curls is %d'%cap_uri_num
	print 'The number of location is %d'%location_num
	print 'The number of log is %d'%log_num

# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()

print 'finished'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
