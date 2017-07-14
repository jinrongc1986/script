#-*- coding:utf-8 -*-
import os,subprocess
import sys,getopt
import json

#默认参数选择
filedomain='match_cp_host.conf'
server_ip='114.114.114.114'
port=53
x=0
y=0
z=0
fail_noanswer=[]
fail_notlocal=[]
mode='all'

#参数选择
opts,arts = getopt.getopt(sys.argv[1:],"lvhap:i:")
for op,value in opts:
    if op=="-l":
        mode='live'
    elif op=="-v":
        mode='demand'
    elif op=="-a":
        mode='all'
    elif op=="-h":
        mode='http'
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
    if '222.30.49.25' in stdout:
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
data=json.load(f)
domainlist=[]
if mode=='all':
    domainlist=[i['host'] for i in data['zones']]
elif mode=='live':
    domainlist=[i['host'] for i in data['zones'] if i['type']=='cnc_live']
elif mode=='demand':
    domainlist=[i['host'] for i in data['zones'] if i['type']=='cnc_demand']
elif mode=='http':
    domainlist=[i['host'] for i in data['zones'] if i['type']=='cnc_http']
dllen=len(domainlist)
for i in range(dllen):
    domain=domainlist[i]
    result=check_dns(domain,server_ip,port)
    print result
print "failed:"
print fail_notlocal
print "noanswer:"
print fail_noanswer
print 'total domain counter : %d'%dllen
print 'total sucess : %d'%x
print 'total not local : %d'%z
print 'total no A answer : %d'%y
