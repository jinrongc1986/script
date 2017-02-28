#!/usr/bin/env python  
#encoding: utf-8  
#description: get local ip address  
  
import os  
import socket, fcntl, struct  
  
def get_ip1():  
    #注意外围使用双引号而非单引号,并且假设默认是第一个网卡,特殊环境请适当修改代码  
    ip = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read().split('\n')[0]
    return ip  
  
#另一种方法, 只需要指定网卡接口, 我更倾向于这个方法  
def get_ip2(ifname):  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])  
  
if __name__ == '__main__':  
    print get_ip1()
    print get_ip2('eth0')  
