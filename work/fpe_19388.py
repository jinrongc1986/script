#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import xmlrpclib

XML_RPC = "http://localhost:19388/RPC2"
g_xmlrpc_proxy = xmlrpclib.ServerProxy(XML_RPC)

def pkt_in(arg):
    pkt_in_rpc=g_xmlrpc_proxy.pkt_in(arg)
    print (pkt_in_rpc)

def proxyed(arg):
    proxyed_rpc=g_xmlrpc_proxy.proxyed(arg)
    print (proxyed_rpc)

def exec_insert():
    try :
        sys.argv[1]
        if sys.argv[1].split(':')[0] not in ['on','off','sm300','sm200']:
            print "wrong argv, must be: on:xxxx(ruleid) off:xxxx(ruleid)"
            sys.exit(0)
        else :
            pkt_in_(arg)
    except Exception as e:
        print "need argv: on:xxxx off:xxxx"
        print "exec default configuration"
        insert_power(arg)
    

if __name__=='__main__':
    arg1 = {
        "pkt":"GET /20180103154407/0469d8b7580dc654fe75d85dee4c569d/ymusic/9313/cfac/35ad/332d8257716efd86d075809e61cfd5d5.mp3 HTTP/1.1\r\nHost: m10.music.126.net\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nAccept-Encoding: identity;q=1, *;q=0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36\r\nAccept: */*\r\nAccept-Language: zh-CN,zh;q=0.9\r\nRange: bytes=0-\r\n","src_ip":"30.30.33.2"
        }
    arg2 = {"url":"http://m10.music.126.net/20180103154407/0469d8b7580dc654fe75d85dee4c569d/ymusic/9313/cfac/35ad/332d8257716efd86d075809e61cfd5d5.mp3","range":"0-","src_ip":"30.30.32.2"} #不能用，暂不实现
    arg3 = {
        "pkt":"GET /molbin/iss-loc/amcore/content/00010005/000522/smldat.cab HTTP/1.1\r\nHost: download.mcafee.com\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nAccept-Encoding: identity;q=1, *;q=0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36\r\nAccept: */*\r\nAccept-Language: zh-CN,zh;q=0.9\r\n","src_ip":"30.30.33.2"}
    proxyed_arg = {"url":"http://m8c.music.126.net/20180115143631/a770e6c019c5524769d87ad85e9d7ca0/ymusic/ae4b/4be3/6991/e3bcfa28cb569cc2e235051205b8ef97.mp","mode":"1","callback":"30.30.32.2"} #不能用，暂不实现
    #pkt_in(arg1)
    proxyed(proxyed_arg)
