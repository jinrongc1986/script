#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import xmlrpclib

XML_RPC = "http://localhost:19390/RPC2"
g_xmlrpc_proxy = xmlrpclib.ServerProxy(XML_RPC)

def matchd_furl(arg):
    pkt_in_rpc=g_xmlrpc_proxy.matchd.furl(arg)
    print (pkt_in_rpc)


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
        "url":"http://m10.music.126.net/20180103154407/0469d8b7580dc654fe75d85dee4c569d/ymusic/9313/cfac/35ad/332d8257716efd86d075809e61cfd5d5.jpg","src_ip":"30.30.32.2","user_agent":"iphone"
        }
    matchd_furl(arg1)
