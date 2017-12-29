#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import xmlrpclib

XML_RPC = "http://localhost:19380/RPC2"
g_xmlrpc_proxy = xmlrpclib.ServerProxy(XML_RPC)

def insert_power(arg):
    power=g_xmlrpc_proxy.turn_ruleid(arg)
    print (power)

def exec_insert():
    try :
        sys.argv[1]
        if sys.argv[1].split(':')[0] not in ['on','off','sm300','sm200']:
            print "wrong argv, must be: on:xxxx(ruleid) off:xxxx(ruleid)"
            sys.exit(0)
        else :
            insert_power(arg)
    except Exception as e:
        print "need argv: on:xxxx off:xxxx"
        print "exec default configuration"
        insert_power(arg)
    

if __name__=='__main__':
    arg = {'on':"1124,4803",
        'off':"3524,3281",
        "sm300":"",
        "sm100":"1124"
        }
    exec_insert()
