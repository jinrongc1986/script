#-*- coding:utf-8 -*-
import os,subprocess,time
from time import sleep
import make_http_pcap

def create_bridge():
    path=os.path.split(os.path.realpath(__file__))[0]
    cmd='bash %s/start_mirror.sh'
    cb = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    cb.communicate()
    print ("创建bridge成功")

def get_local_ip(nic='br100'):
    ip = os.popen(("ifconfig %s | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1")%nic).read().split('\n')[0] 
    print ("%s ip : %s"%(nic,ip))
    return ip

def tcprew(ip):
    iplist=ip.split('.')
    iplist[3]= str(int(iplist[3])+1)
    ipnew='.'.join(iplist)
    cmd='tcprewrite --srcipmap=%s:%s -i http_head.pcap -o bigFlows.pcap'%(ip,ipnew)
    tcprw= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tcprw.communicate()
    print ("rewrite src_ip to : %s"%ipnew)

def tcprep(speed=1,loop=2):
    cmd='tcpreplay -K -i veth1 --mbps %d  --loop %d  --unique-ip bigFlows.pcap'%(speed,loop)
    tcprp= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tcprp.communicate()
    print ("tcpreplay 执行成功，请确认回源队列！")

def del_bridge():
    cmd='brctl delif br-xedge eth1'
    del_br=subprocess.call(cmd, shell=True)
    print ("清除bridge成功")
    
if __name__=='__main__' :
    make_http_pcap.make_http_pcap()
    create_bridge()
    br100_ip=get_local_ip(nic='br100')
    tcprew(br100_ip)
    tcprep(speed=1,loop=2)
    del_bridge() 
