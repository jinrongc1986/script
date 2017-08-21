#-*- coding:utf-8 -*-
import os,subprocess
import sys,getopt
import json

#默认参数选择
server_ip='114.114.115.115'
#参数选择
opts,arts = getopt.getopt(sys.argv[1:],"t:s:e:")
for op,value in opts:
    if op=="-t":
        times=value
        times=int(value)
    elif op=="-s":
        start=value
        start=int(value)
    elif op=="-e":
        end=value
        end=int(end)

def check_dns(host,server_ip):
    cmd='dig %s @%s'%(host,server_ip)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout=p.stdout.read()
    #print(stdout)

for x in range(start,end+1):
    for i in range (0,times): 
        y=str(x).zfill(5)
        host='WWW.%s.com'%y
        check_dns(host,server_ip)
