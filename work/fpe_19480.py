#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import xmlrpclib
import time

debug = 1
XML_RPC = "http://localhost:19480/RPC2"
g_xmlrpc_proxy = xmlrpclib.ServerProxy(XML_RPC)

def date_now():
    timenow=time.localtime(time.time())
    return time.strftime("%Y-%m-%d",timenow)

def insert_task(url):
    global debug
    msg = {"nodeid": "101", "token": "3356", "action": "set_task", "var0": "1","var1":url}
    print msg
    out = g_xmlrpc_proxy.callback(msg)
    if debug :
        print url
        print out
    return out
    
def bulk_insert():
    global debug
    filename='/home/dcwork/precache/listC/%s_part-00000'%date_now()
    f = open(filename,'r')
    lines=f.readlines()
    for line in lines:
        url = line.split("\t")[-1].strip()
        out=insert_task(url)
        if "'results': '1'" not in str(out) & debug:
            print '#'*20
            print url
            print out
            print '#'*20
        
def exec_insert():
    try :
        if sys.argv[1] == "today":
            bulk_insert()
        elif sys.argv[1].split('http://')[1]:
            url = sys.argv[1]
            insert_task(url)
        else :
            print "wrong url"
            sys.exit(0)
    except Exception as e:
        print "need url input or input 'today'"
    

if __name__=='__main__':
    exec_insert()
