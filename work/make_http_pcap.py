#-*- coding:utf-8 -*-
import os,subprocess,time
from time import sleep
import get_http_url


def make_http_pcap():
    get_http_url.geturls();
    print ("开始抓包...")
    capture="tcpdump -i eth0 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x48454144' -w http_head.pcap"
    dump = subprocess.Popen(capture, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    f=open('./urls.txt','r')
    urls=f.readlines()
    print ("开始发流...")
    for url in urls:
        url=url.strip()
        cmd="wget '%s' --spider"%url
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sleep(5)
    dump.terminate()
    print ("生成最新的http_head.pcap成功")

if __name__=='__main__' :
    make_http_pcap()
