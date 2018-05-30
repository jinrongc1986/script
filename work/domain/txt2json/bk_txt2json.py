#coding:utf-8
from collections import defaultdict
import json

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
    #zone_dict = {}
    cnc_dict = {}
    txt2json = Txt2Json()
    cnc_http = txt2json.cncHttp()
    cnc_demand = txt2json.cncDemand()
    cnc_live = txt2json.cncLive()
    cnc_dict["cnc_http"] = cnc_http
    cnc_dict["cnc_demand"] = cnc_demand
    cnc_dict["cnc_live"] = cnc_live
    f = open('./zone_list.json','r')
    zone_json = json.load(f)
    zone_dict = zone_json
    for key, value in zone_dict.items():
        if key == "zone":
            for key1, value1 in value.items():
                if key1 == "cnc_http":
                    value[key1] = cnc_http
                if key1 == "cnc_demand":
                    value[key1] = cnc_demand
                if key1 == "cnc_live":
                    value[key1] = cnc_live
        break
    f.close()
    f = open('./txt2json.js', 'w')
    json.dump(zone_dict, f, indent=4)         
    f.close()


