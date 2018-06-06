#coding:utf-8
from collections import defaultdict
import json
import time
from ftplib import FTP

def getfile():
    ftp=FTP()
    timeout=30
    port =21
    ftp.connect("192.168.1.222",port,timeout)
    ftp.login()
    ftp.cwd('cds/ftp/cnc-up/')
    filesname=ftp.nlst()
    httpfile='feixiang_pic_domain_'
    demandfile='feixiang_vod1_domain_'
    livefile='feixiang_vod2_domain_'
    for filename in filesname:
        if "feixiang_pic_domain_" in filename:
            if filename > httpfile:
                httpfile=filename
        if 'feixiang_vod1_domain_' in filename:
            if filename > demandfile:
                demandfile=filename
        if 'feixiang_vod2_domain_' in filename:
            if filename > livefile:
                livefile=filename
        else:
            pass
    print ("update zone_list.json from following files:")
    print (httpfile,demandfile,livefile)
    bufsize=1024
    ftp.retrbinary("RETR " + httpfile , open(httpfile,"wb").write , bufsize)
    ftp.retrbinary("RETR " + demandfile , open(demandfile,"wb").write , bufsize)
    ftp.retrbinary("RETR " + livefile , open(livefile,"wb").write , bufsize)
    ftp.quit()
    return (httpfile,demandfile,livefile)

class Txt2Json(object):

    def __init__(self,arg):
        self.dd_http = defaultdict(list)
        self.dd_demand = defaultdict(list)
        self.dd_live = defaultdict(list)
        self.httpfile = arg[0]
        self.demandfile = arg[1]
        self.livefile = arg[2]

    def cncHttp(self):
        f = open(self.httpfile, 'r')
        hosts = f.readlines()

        for host in hosts:
            host = host.strip()
            host_split = host.split(".")
            host_postfix = "." + host_split[-2] + "." + host_split[-1]
            host_prefix = ".".join(host_split[:-2])
            self.dd_http[host_postfix].append(host_prefix)
        return self.dd_http
        f.close()

    def cncDemand(self):
        f = open(self.demandfile, 'r')  
        hosts = f.readlines()
    
        for host in hosts:
            host = host.strip()
            host_split = host.split(".")
            host_postfix = "." + host_split[-2] + "." + host_split[-1]
            host_prefix = ".".join(host_split[:-2])
            self.dd_demand[host_postfix].append(host_prefix)
        return self.dd_demand
        f.close()

    def cncLive(self):
        f = open(self.livefile, 'r')  
        hosts = f.readlines()
    
        for host in hosts:
            host = host.strip()
            host_split = host.split(".")
            host_postfix = "." + host_split[-2] + "." + host_split[-1]
            host_prefix = ".".join(host_split[:-2])
            self.dd_live[host_postfix].append(host_prefix)
        return self.dd_live
        f.close()

if __name__=='__main__':
    print ("Please update zone_list.json if other domains has been changed except cnc")
    filesname=getfile()
    txt2json = Txt2Json(filesname)
    cnc_http = txt2json.cncHttp()
    cnc_demand = txt2json.cncDemand()
    cnc_live = txt2json.cncLive()
    fold = open('./zone_list.json', 'r')
    data=json.load(fold)
    data['zone']["cnc_http"] = cnc_http
    data['zone']["cnc_demand"] = cnc_demand
    data['zone']["cnc_live"] = cnc_live
    update_time=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    data['time']=update_time
    version=data['version']
    version_new=version.split('.')[0]+'.'+str(int(version.split('.')[1])+1)
    data['version']=version_new
    f = open('./zone_list_new.json', 'w')
    json.dump(data, f, indent=4)         
    f.close()
