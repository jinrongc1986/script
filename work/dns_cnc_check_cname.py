#-*- coding:utf-8 -*-
import os,subprocess
import sys,getopt
import json

#默认参数选择
filedomain='domain_cnc_video_demand.txt'
server_ip='30.30.32.3'
port=53
x=0
y=0
z=0
fail_noanswer=[]
fail_notlocal=[]

#参数选择
opts,arts = getopt.getopt(sys.argv[1:],"lvhop:i:")
for op,value in opts:
    if op=="-l":
        filedomain='domain_cnc_video_live.txt'
    elif op=="-v":
        filedomain='domain_cnc_video_demand.txt'
    elif op=="-o":
        filedomain='host.txt'
    elif op=="-h":
        filedomain='domain_cnc_http.txt'
    elif op=="-i":
        server_ip=value
    elif op=="-p":
        port=value
        port=int(port)

def check_dns(cnc_domain,server_ip,port=53):
    cmd='dig %s @%s -p %d'%(cnc_domain,server_ip,port)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout=p.stdout.read()
    global x
    global y
    global z
    global faillist
    if '192.168.1.17' in stdout:
        x = x + 1
        return '%s is OK'%(cnc_domain)
    elif 'ANSWER: 0, AUTHORITY' in stdout:
        y = y + 1
        fail_noanswer.append('%s'%cnc_domain)
        return '~~~~~~~~~~~~~~~~~~~~~~~~~~~%s is NoAnswer'%cnc_domain
    else:
        z = z + 1
        fail_notlocal.append('%s'%cnc_domain)
        return '###########################%s is NotLocal'%cnc_domain

f=open(r"/home/git/script/work/%s"%filedomain,"r+")
domainlist=[]
domainlist=f.readlines()
dllen=len(domainlist)
for i in range(dllen):
    domain=domainlist[i].split('\n')[0]
    result=check_dns(domain,server_ip,port)
    print result
print 'total domain counter : %d'%dllen
print 'total sucess : %d'%x
print 'total not local : %d'%z
print fail_notlocal
print 'total no answer : %d'%y
print fail_noanswer
