#!/usr/bin/python
#coding=utf-8
import subprocess
import paramiko
import pexpect

def sshclient_execmd(port, execmd, hostname='rhelp.fxdata.cn', username='root', password='FxData!Cds@2016_'):
    paramiko.util.log_to_file("./paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command (execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
    output= stdout.read()
    s.close()
    return output

def get_port(sn):
    cmd='''mysql -N -e "select rhelp from ordoac.feedback where sn='CAS0530000152'"  -h 192.168.1.12 -uselector -pfxdata_Select-2016 -P 3305'''
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ports=p.stdout.readlines()
    port=ports[0].strip().split(':')[2]
    return port

def geturls(sn='CAS0530000152'):
    print ("请等待连接远程服务器...")
    port=int(get_port(sn))
    cmd='rm -f /tmp/test_jinrongc.txt'
    cmd1='mysql -N  -e  "select uri from cache.video_cache order by create_time desc limit 5 ;" >> /tmp/test_jinrongc.txt'
    cmd2='mysql -N  -e  "select uri from cache.mobile_cache order by create_time desc limit 5 ;" >> /tmp/test_jinrongc.txt'
    cmd3='mysql -N  -e  "select uri from cache.http_cache order by create_time desc limit 5 ;" >> /tmp/test_jinrongc.txt'
    sshclient_execmd(port,cmd)
    print ("等待生成数据...")
    sshclient_execmd(port,cmd1)
    sshclient_execmd(port,cmd2)
    sshclient_execmd(port,cmd3)

    
    #child=pexpect.spawn('scp -P %d  root@rhelp.fxdata.cn:/tmp/test_jinrongc.txt /tmp/test_jinrongc.txt'%port)
    child=pexpect.spawn('scp -P %d  root@rhelp.fxdata.cn:/tmp/test_jinrongc.txt ./urls.txt'%port)
    child.expect("root@rhelp.fxdata.cn's password:")
    child.sendline("FxData!Cds@2016_")
    child.expect(pexpect.EOF)

    sshclient_execmd(port,cmd)
    
    print('生成并同步到本地 urls.txt 成功')

if __name__=='__main__':
    geturls()
