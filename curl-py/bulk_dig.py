#-*- coding:utf-8 -*-
import os,subprocess,time
cmd='dig www.163.com @202.101.172.35'
for i in range(1,100):
    cmd1=cmd
    p = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print p.stdout.read()
    time.sleep(2)
