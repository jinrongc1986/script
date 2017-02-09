#-*- coding: utf-8 -*-
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('30.30.32.3',port=22,username = 'root',password='FxData!Cds@2016_',timeout=5)
cmd = 'ls'    #进入用户目录home
stdin,stdout,stderr = ssh.exec_command(cmd)
#cmd = 'ls >test.txt'  #管道，ls命名的输出到文件test里面
#stdin,stdout,stderr = ssh.exec_command(cmd)
print (stdout)
