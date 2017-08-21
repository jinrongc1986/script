# -*- coding:utf-8 -*-  
import xmlrpclib
import subprocess 
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
def tag_info_ftop(url,src_ip,user_agent):
    arg = {'url': url, 'src_ip': src_ip, 'user_agent': user_agent}
    tag_info=g_xmlrpc_proxy.matchd.furl(arg)
    return tag_info[0]

def compare_tag(tag_am,tag_info):
    flag=False
    if not int(tag_am['cp'])==tag_info['cp']:
        flag=True
    if not int(tag_am['user_net'])==tag_info['user_net']: 
        flag=True
    if not int(tag_am['ua_type'])==tag_info['ua_type']: 
        flag=True
    if not int(tag_am['ctype'])==tag_info['ctype']: 
        flag=True
    return flag
    
if __name__=='__main__':
    url=["http://pl7.live.panda.tv/live_panda/a7b62f67bd30b4d681e80365437ea5ec_mid.flv"]
    src_ip='30.30.32.4'
    user_agent='iphone'
    for i in range (0,1):
        tag_am=amatch(url[i],user_agent)
        tag_info=tag_info_ftop(url[i],src_ip,user_agent)
        flag=compare_tag(tag_am,tag_info)
        if(flag) :
            print(url[i],src_ip,user_agent)
            print("id:%d amatch: ctype:%s,cp:%s,user_agent:%s,user_net:%s"%(i,tag_am['ctype'],tag_am['cp'],tag_am['user_agent'],tag_am['user_net']))
            print("id:%d infosd: ctype:%s,cp:%s,user_agent:%s,user_net:%s"%(i,tag_info['ctype'],tag_info['cp'],tag_info['user_agent'],tag_info['user_net']))
        else :
            print ("id:%d matched"%i)
