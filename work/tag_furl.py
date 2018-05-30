#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import xmlrpclib
import subprocess 
from user_agent import generate_user_agent
from url_analysis import url_analysis

XML_RPC = "http://localhost:19390/RPC2"
g_xmlrpc_proxy = xmlrpclib.ServerProxy(XML_RPC)

def amatch(url,ua):
    cmd="/home/icache/amatch --url='%s' --user_agent='%s'"%(url,ua)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result=p.stdout.read()
    #result.split('\n')[:-1]
    dic=dict()
    data=result.split('\n')[:-1] #最后有一空行
    for i in range(len(data)):
        x=data[i].split(':',1)[0].strip()
        y=data[i].split(':',1)[1].strip()
        dic[x]=y
    return dic
    #return result 
def tag_info_furl(url,src_ip,user_agent):
    arg = {'url': url, 'src_ip': src_ip, 'user_agent': user_agent}
    tag_info=g_xmlrpc_proxy.matchd.furl(arg)
    print (tag_info)
    return tag_info[0]

def tag_info_whitecache(host,path,filename,extname):
    arg = {'host': host, 'path':path, 'filename':filename, 'extname':extname}
    tag_info=g_xmlrpc_proxy.matchd.whitecache(arg)
    print (tag_info)
    return tag_info[0]

def tag_info_ice(src_ip,user_agent):
    arg = {'src_ip': src_ip, 'user_agent': user_agent}
    tag_info=g_xmlrpc_proxy.matchd.get_tag(arg)
    print (tag_info)
    return tag_info[0]

def compare_tag(tag_am,tag_info):
    flag=False
    try :
        if tag_info['cp'] and not int(tag_am['cp'])==tag_info['cp']:
            flag=True
    except :
        pass
    try :
        if tag_info['user_net'] and not int(tag_am['user_net'])==tag_info['user_net']: 
            flag=True
    except :
        pass
    try :
        if tag_info['ua_type'] and not int(tag_am['ua_type'])==tag_info['ua_type']: 
            flag=True
    except :
        pass
    try :
        if tag_info['ctype'] and not int(tag_am['ctype'])==tag_info['ctype']: 
            flag=True
    except :
        pass
    return flag

def furl(match):    
    src_ip='30.30.32.4'
    user_agent= generate_user_agent()
    f = open("./url.txt")
    i=0
    failcnt=0
    total=len(f.readlines())
    f.seek(0,0)
    for url in f.readlines():
        url=url.strip()
        tag_info=tag_info_furl(url,src_ip,user_agent)
        if match=='match':
            tag_am=amatch(url,user_agent)
            flag=compare_tag(tag_am,tag_info)
            #flag=0
            if(flag) :
                print(url,src_ip,user_agent)
                print("id:%d amatch: ctype:%s,cp:%s,ua_type:%s,user_net:%s"%(i,tag_am['ctype'],tag_am['cp'],tag_am['ua_type'],tag_am['user_net']))
                print("id:%d infosd: ctype:%s,cp:%s,ua_type:%s,user_net:%s"%(i,tag_info['ctype'],tag_info['cp'],tag_info['ua_type'],tag_info['user_net']))
                failcnt += 1
            #else :
            #    print ("id:%d matched"%i)
            i += 1
            sys.stdout.write('\rcurrent id:%5d, total cnt:%6d, failed cnt:%5d'%(i,total,failcnt))
            sys.stdout.flush()
        else :
            i += 1
            sys.stdout.write('\rcurrent id:%5d, total cnt:%6d, failed cnt:%5d'%(i,total,failcnt))
            sys.stdout.flush()

def whitecache(match):    
    src_ip='30.30.32.4'
    user_agent= generate_user_agent()
    #user_agent='iphone'
    f = open("./url.txt")
    i=0
    failcnt=0
    total=len(f.readlines())
    f.seek(0,0)
    for url in f.readlines():
        url=url.strip()
        try :
            info=url_analysis(url)
            host=info["host"]
            path=info["path"]
            filename=info["filename"]
            extname=info['extname']
            tag_info=tag_info_whitecache(host,path,filename,extname)
            if match=='match':
                tag_am=amatch(url,user_agent)
                flag=5
                try :
                    flag=int(tag_info['whitecache'])
                except Exception as e:
                    print (e)
                if flag==0 :
                    pass
                    #print (tag_info)
                    #print ("黑名单：%s"%url)
                    #print ("amtch cancached:%s"%tag_am['mpath|set_en|cancached'].split('|')[2])
                elif flag==1 :
                    pass
                    #print("白名单：%s"%url)
                elif flag==-1 :
                    print (tag_info)
                    print ("无法匹配：%s"%url)
                    print ("amtch cancached:%s"%tag_am['mpath|set_en|cancached'].split('|')[2])
                    failcnt += 1
                i += 1
                sys.stdout.write('\rcurrent id:%5d, total cnt:%6d, failed cnt:%5d'%(i,total,failcnt))
                sys.stdout.flush()
            else :
                i += 1
                sys.stdout.write('\rcurrent id:%5d, total cnt:%6d'%(i,total))
                sys.stdout.flush()
        except Exception as e:
            print (i)

def get_tag(match,total=10000):    
    src_ip='30.30.32.4'
    user_agent= generate_user_agent()
    failcnt=0
    url="http://www.baidu.com/justfortest.jpg"
    for i in range(0,total):
        tag_info=tag_info_ice(src_ip,user_agent)
        if match=='match':
            tag_am=amatch(url,user_agent)
            flag=compare_tag(tag_am,tag_info)
            #flag=0
            if(flag) :
                print(url,src_ip,user_agent)
                print("id:%d amatch: ctype:%s,cp:%s,ua_type:%s,user_net:%s"%(i,tag_am['ctype'],tag_am['cp'],tag_am['ua_type'],tag_am['user_net']))
                print("id:%d get_tag: ua_type:%s,user_net:%s"%(i,tag_info['ua_type'],tag_info['user_net']))
                failcnt += 1
            #else :
            #    print ("id:%d matched"%i)
            i += 1
            sys.stdout.write('\rcurrent id:%5d, total cnt:%6d, failed cnt:%5d'%(i,total,failcnt))
            sys.stdout.flush()
        else :
            i += 1
            sys.stdout.write('\rcurrent id:%5d, total cnt:%6d'%(i,total))
            sys.stdout.flush()

if __name__=='__main__':
    #set type and match
    match='match'
    try :
        sys.argv[1]
        if sys.argv[1] not in ['furl','get_tag','whitecache']:
            print "wrong argv, must be: furl or get_tag or whitecache and match or nomatch"
            sys.exit(0)
    except Exception as e:
        print "need argv: furl or get_tag or whitecache"
        sys.exit(0)
    try :
        if sys.argv[2] in ['match','nomatch']:
            match=sys.argv[2]
    except Exception as e:
        print ('default do match between  %s and amatch'%sys.argv[1])
    #start do
    if sys.argv[1] == "furl" :
        furl(match)
    elif sys.argv[1] == "get_tag" :
        get_tag(match)
    elif sys.argv[1] == "whitecache" :
        whitecache(match)
