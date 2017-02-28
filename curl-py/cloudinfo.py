#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys,time,getopt
import commands
ipaddr=''
opts,arts = getopt.getopt(sys.argv[1:],"hi:")
for op,value in opts:
        if op=="-i":
                ipaddr=value
        elif op=="-h":
                print "请输入需要检查的云友IP"
                sys.exit()
def getcnt(ipaddr):
        cmd="/home/icache/icached cloudinfo"
        p=commands.getoutput(cmd)
        listA=p.split('\n')
        for i in range (len(listA)):
                if ipaddr in listA[i]:
                        cnt=listA[i].split(',')[3]
        return cnt

def timenow():
	ISOTIMEFORMAT='%Y-%m-%d %X'
	return time.strftime( ISOTIMEFORMAT, time.localtime() )

if ipaddr=='':
	print '请输入参数-i 云友IP'
	exit()
starttime=timenow()
print 'start time at:%s'%starttime
lastcnt=getcnt(ipaddr)
print '当前diff大小：%s'%lastcnt
print 'running...'
#每2秒执行一次检测
while True:
        newcnt=getcnt(ipaddr)
        if lastcnt!=newcnt:
                endtime=timenow()
		break
	else :
		time.sleep(2)
print 'update at time:%s'%endtime
f=open('cloudinfo.log','wb')
echocmd='update at time:%s'%endtime
print >>f,echocmd
print 'update to %s'%newcnt
