#!/usr/bin/python
#-*- coding:utf-8 -*-
import subprocess,urllib2
import os,sys,re
import time
from threading import Thread
import getopt
import paramiko
# 参数输入
opts,arts = getopt.getopt(sys.argv[1:],"hlru:t:n:c:")
url="http://20.20.20.4/test/0001.mp4?0001"
cycles='1'
total=1
client='3'
location="local"
filetype='mp4'
for op,value in opts:
    if op=="-u":
        url=value
    elif op=="-t":
        filetype=value
    elif op=="-n":
        total=value
        total=int(total)
    elif op=="-l":
        location="local"
    elif op=="-r":
        location="remote"
    elif op=="-c":
        client=value
    elif op=="-h":
        print "-u URL like 'http://20.20.20.4/test/'"
        print "-t filetype like 'mp4'"
        print "-n total like 100"
        print "-l local like local"
        print "-l remote like remote"
        print "-c clinet like 5"
        exit()
def curl_bulk_set(url,client,cycles):
    # curl_loader参数设置
    f=open(r"/home/git/script/curl-py/curl_base.conf","r+")
    flist=[]
    flist=f.readlines()
    flist[2]='CLIENTS_NUM_MAX='+client+'\n'
    flist[3]='CLIENTS_NUM_START='+client+'\n'
    flist[9]='CYCLES_NUM='+cycles+'\n'
    flist[14]='URL='+url+'\n'
    f=open(r"/home/git/script/curl-py/curl_base.conf","w+")
    f.writelines(flist)

def curl_bulk_exec(location):
    # 执行curl命令
    if location=="local":
        cmd = "/home/curl-loader-0.56/curl-loader -f /home/git/script/curl-py/curl_base.conf"
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #p = subprocess.Popen(cmd, shell=True)
        #p.communicate(input=None)
        p.wait()
    elif location=="remote":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('30.30.32.4',port=22,username = 'root',password='123456',timeout=5)
        cmd = '/home/git/curl-loader-0.56/curl-loader -f /home/git/script/curl-py/curl_base.conf'    #进入用户目录home/git
        stdin,stdout,stderr = ssh.exec_command(cmd)
if __name__ == "__main__":
    ISOTIMEFORMAT='%Y-%m-%d %X'
    print time.strftime( ISOTIMEFORMAT, time.localtime() )
    print 'running...'
    for i in range(506,total+1):
        print 'round:%d'%i
        a=str(i).zfill(4)
        url="http://20.20.20.4/test/%s.%s?%s"%(a,filetype,a)
        curl_bulk_set(url,client,cycles)
        curl_bulk_exec(location)
        #time.sleep(0.2)
        if 1000<i<2001:
            print 'dup round:%d'%i
            curl_bulk_set(url,'4',cycles)
            curl_bulk_exec(location)
            time.sleep(0.2)
    print 'finished'
    print time.strftime( ISOTIMEFORMAT, time.localtime() )
