#coding:utf-8
from collections import defaultdict
import json
import time

class Txt2Json(object):

    def __init__(self):
        self.dd_http = defaultdict(list)
        self.dd_demand = defaultdict(list)
        self.dd_live = defaultdict(list)

    def cncHttp(self):
        f = open('./feixiang_pic_domain_2018-05-02_1.txt', 'r')
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
        f = open('./feixiang_vod1_domain_2018-05-02_1.txt', 'r')  
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
        f = open('./feixiang_vod2_domain_2018-05-02_1.txt', 'r')  
        hosts = f.readlines()
    
        for host in hosts:
            host = host.strip()
            host_split = host.split(".")
            host_postfix = "." + host_split[-2] + "." + host_split[-1]
            host_prefix = ".".join(host_split[:-2])
            self.dd_live[host_postfix].append(host_prefix)
        return self.dd_demand
        f.close()

if __name__=='__main__':
    zone_dict = {}
    cnc_dict = {}
    txt2json = Txt2Json()
    cnc_http = txt2json.cncHttp()
    cnc_demand = txt2json.cncDemand()
    cnc_live = txt2json.cncLive()
    zone_dict["zone"] = cnc_dict
    f1 = open('./zone_list.json', 'r')
    data=json.load(f1)
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
