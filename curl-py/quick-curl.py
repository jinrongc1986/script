#-*- coding:utf-8 -*-
import subprocess,urllib2
import os,sys,re
import time
from threading import Thread
import getopt
import paramiko
# 参数输入
opts,arts = getopt.getopt(sys.argv[1:],"hlru:n:c:i:")
url=""
total=1
location="remote"
for op,value in opts:
        if op=="-u":
                url=value
        elif op=="-n":
                total=value
        elif op=="-l":
                location="local"
        elif op=="-r":
                location="remote"
        elif op=="-c":
                client=value
# curl_loader参数设置
f=open(r"/home/jinrong/curl-py/curl_base.conf","r+")
flist=[]
flist=f.readlines()
print flist[0]
flist[2]='CLIENTS_NUM_MAX='+client+'\n'
flist[9]='CYCLES_NUM='+total+'\n'
flist[14]='URL='+url+'\n'
f=open(r"/home/jinrong/curl-py/curl_base.conf","w+")
f.writelines(flist)

# 执行curl命令
ISOTIMEFORMAT='%Y-%m-%d %X'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
print 'running...'
if location=="local":
        cmd = "/home/curl-loader-0.56/curl-loader -f /home/jinrong/curl-py/curl_base.conf"
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
elif location=="remote":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('30.30.32.4',port=22,username = 'root',password='123456',timeout=5)
        cmd = '/home/curl-loader-0.56/curl-loader -f /home/jinrong/curl-py/curl_base.conf'    #进入用户目录home
        stdin,stdout,stderr = ssh.exec_command(cmd)

print 'finished'
print time.strftime( ISOTIMEFORMAT, time.localtime() )
