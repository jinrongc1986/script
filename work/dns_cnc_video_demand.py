#-*- coding:utf-8 -*-
import os,subprocess
x=0
y=0
def check_dns(cnc_domain):
    cmd='dig %s @20.20.20.2'%cnc_domain
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout=p.stdout.read()
    global y
    global x
    if '192.168.1.' in stdout:
        y = y + 1
        return '%s is OK'%(cnc_domain)
    else:
        x = x + 1
        return '###########################%s is NOK'%cnc_domain

f=open(r"/home/git/script/work/dns_cnc_video_demand.txt","r+")
domainlist=[]
domainlist=f.readlines()
dllen=len(domainlist)
for i in range(dllen):
    domain=domainlist[i].split('\n')[0]
    result=check_dns(domain)
    print result
print 'total sucess : %d'%y
print 'total fail :%d'%x
