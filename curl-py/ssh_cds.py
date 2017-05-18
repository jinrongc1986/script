#!/usr/bin/env python  
#encoding: utf-8
import paramiko,os 
import socket,fcntl,struct
  
def sshclient_execmd(hostname, port, username, password, execmd):  
    paramiko.util.log_to_file("/home/git/script/curl-py/paramiko.log")  
      
    s = paramiko.SSHClient()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
      
    s.connect(hostname=hostname, port=port, username=username, password=password)  
    stdin, stdout, stderr = s.exec_command (execmd)  
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
    #print stdout.read() 
    output= stdout.read()  
    s.close()  
    return output 

      
def cds_init(querycmd, execmd, ip, local_ip): 
    hostname = ip
    port = 22 
    username = 'root'  
    password = 'FxData!Cds@2016_'
    if hostname=='30.30.33.3' or hostname =='20.20.20.2':
        password = '123'
    query_result=sshclient_execmd(hostname, port, username, password, querycmd)
    iptable_restart='/home/icache/configd config iptables'
    judgecmd=execmd.split("'")[1].split(' ',1)[1]
    if judgecmd not in query_result:
        sshclient_execmd(hostname, port, username, password, execmd)
        sshclient_execmd(hostname, port, username, password, iptable_restart)

def cds_init_bk(querycmd, execmd, ip, local_ip): 
    hostname = ip
    port = 22 
    username = 'root'  
    password = 'FxData!Cds@2016_'
    if hostname=='30.30.33.3' or hostname =='20.20.20.2':
        password = '123'
    query_result=sshclient_execmd(hostname, port, username, password, querycmd)
    iptable_restart='service iptables restart'
    #if ('-A INPUT -s %s -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT')%local_ip not in query_result:
    if  execmd not in query_result:
        sshclient_execmd(hostname, port, username, password, execmd)
        sshclient_execmd(hostname, port, username, password, iptable_restart)

def main(execmd, ip, location_ip=''): 
    #import pdb; pdb.set_trace()
    if location_ip=='':
        hostname = ip
    else :
        hostname = location_ip
    port = 22 
    username = 'root'  
    password = 'FxData!Cds@2016_'  
    if hostname=='30.30.33.3' or hostname =='20.20.20.2':
        password = '123'
    #execmd = "/home/icache/icached debug"  
    return sshclient_execmd(hostname, port, username, password, execmd) 

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
def get_ip1():
    #注意外围使用双引号而非单引号,并且假设默认是第一个网卡,特殊环境请适当修改代码
    ip = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read().split('\n')[0]
    return ip

if __name__ == "__main__":  
    #ipaddr=['30.30.32.5','30.30.32.3','20.20.20.2'] 
    ipaddr=['30.30.32.3','20.20.20.2'] 
    local_ip=get_ip1()
    for ip in ipaddr:
        querycmd="cat /etc/icache/iptables"
        execmd = "sed -i '6i -A INPUT -s %s -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/icache/iptables"%local_ip
        cds_init(querycmd,execmd,ip,local_ip)
        execmd = "sed -i '6i -A INPUT -s 30.30.32.2 -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/icache/iptables"
        cds_init(querycmd,execmd,ip,local_ip='30.30.32.2')
        execmd = "sed -i '6i -A INPUT -s 30.30.32.4 -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/icache/iptables"
        cds_init(querycmd,execmd,ip,local_ip='30.30.32.4')
