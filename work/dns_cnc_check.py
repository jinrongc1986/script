#-*- coding:utf-8 -*-
import os,subprocess
import sys,getopt
import json
x=0
y=0
faillist=[]
def check_dns(cnc_domain,port=53):
    cmd='dig %s @20.20.20.2 -p %d'%(cnc_domain,port)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout=p.stdout.read()
    global y
    global x
    global faillist
    if '192.168.1.' in stdout:
        y = y + 1
        return '%s is OK'%(cnc_domain)
    else:
        x = x + 1
        faillist.append('failed:%s'%cnc_domain)
        return '###########################%s is NOK'%cnc_domain
#默认选择
filedomain='domain_cnc_video_demand.txt'
port=53
#参数选择
opts,arts = getopt.getopt(sys.argv[1:],"lvhp:")
for op,value in opts:
    if op=="-l":
        filedomain='domain_cnc_video_live.txt'
    elif op=="-v":
        filedomain='domain_cnc_video_demand.txt'
    elif op=="-h":
        filedomain='domain_cnc_http.txt'
    elif op=="-p":
        port=value
        port=int(port)

f=open(r"/home/git/script/work/%s"%filedomain,"r+")
domainlist=[]
domainlist=f.readlines()
dllen=len(domainlist)
for i in range(dllen):
    domain=domainlist[i].split('\n')[0]
    result=check_dns(domain,port)
    print result
print 'total sucess : %d'%y
print 'total fail :%d'%x
print faillist
