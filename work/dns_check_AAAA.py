#-*- coding:utf-8 -*-
import os,subprocess,sys
x=0
y=0
def check_dns(cnc_domain):
    cmd='dig %s @30.30.32.3'%cnc_domain + ' -t AAAA'
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout=p.stdout.read()
    global y
    global x
    if 'status: NOERROR' in stdout:
        y = y + 1
        return '%s is OK'%(cnc_domain)
    else:
        x = x + 1
        return '###########################%s is NOK'%cnc_domain


f = open(r"./domain_ipswitch.txt", "r+")
domainlist=[]
domainlist=f.readlines()
dllen=len(domainlist)
for i in range(dllen):
    domain=domainlist[i].split('\n')[0]
    result=check_dns(domain)
    print result
print 'total sucess : %d'%y
print 'total fail :%d'%x
