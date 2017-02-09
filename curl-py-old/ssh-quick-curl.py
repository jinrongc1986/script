#-*- coding: utf-8 -*-
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('30.30.32.4',port=22,username = 'root',password='123456',timeout=5)
cmd = '/home/curl-loader-0.56/curl-loader -f /home/jinrongc/curl-py/curl_base.conf'    #进入用户目录home
stdin,stdout,stderr = ssh.exec_command(cmd)
#cmd = 'ls >test.txt'  #管道，ls命名的输出到文件test里面
#stdin,stdout,stderr = ssh.exec_command(cmd)
