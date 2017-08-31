# -*- coding:utf-8 -*-
import os
import subprocess
from time import sleep
import get_http_url
import json


def make_http_pcap(flag='all'):
    get_http_url.geturls();
    print ("开始抓包...")
    capture = "tcpdump -i eth0 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x48454144'\
                -w http_head.pcap"
    dump = subprocess.Popen(capture, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    f = open('./urls.txt', 'r')
    urls = f.readlines()
    print ("开始发流...")
    for url in urls:
        url = url.strip()
        if flag == 'all':
            cmd = "wget '%s' --spider" % url
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        elif flag == 'cnc':
            if url_analysis(url):
                cmd = "wget '%s' --spider" % url
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
    sleep(5)
    dump.terminate()
    print ("生成最新的http_head.pcap成功")


def url_analysis(url):
    uri = url.split('//')[1].split('?')[0]
    host = uri.split('/')[0]
    f = open('/home/cnc_export/cnc_host.conf', 'r')
    data = json.load(f)
    wlist = data["white_portal"]
    for white in wlist:
        try:
            if white == host:
                return True
        except Exception as e:
            print e
            pass
    return False


if __name__ == '__main__':
    make_http_pcap()
