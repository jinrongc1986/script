#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import xmlrpclib

XML_RPC = "http://localhost:19388/RPC2"
g_xmlrpc_proxy = xmlrpclib.ServerProxy(XML_RPC)

def pkt_in(arg):
    pkt_in_rpc=g_xmlrpc_proxy.pkt_in(arg)
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
    arg = {
        'pkt':'GET /112.13.107.240/6976C980B314D71E7DF002456/03000A01005A44A08A720641FCADAB3E1D057F-8306-26B2-D91D-53040F1A09B3.mp4?ali_redirect_domain=vali-dns.cp31.ott.cibntv.net&amp;ccode=0502&amp;duration=212&amp;expire=18000&amp;psid=7155cbe6d271ee9d24f171ac02e2201f&amp;showid=6aefbfbdefbfbdd2b321&amp;ups_client_netip=7010452c&amp;ups_ts=1514516217&amp;ups_userid=&amp;utid=U98KEsMMvggCAW8AXbpLi9cT&amp;vid=XMzI2ODY2MTA1Mg%3D%3D&amp;vkey=A713a5f113cb9e84d837484de6c69f51e HTTP/1.1\
Host: 192.168.2.21\
Connection: keep-alive\
Pragma: no-cache\
Cache-Control: no-cache\
Accept-Encoding: identity;q=1, *;q=0\
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36\
Accept: */*\
Referer: http://v.youku.com/v_show/id_XMzI2ODY2MTA1Mg==.html?spm=a2hww.20027244.m_250036.5~5!2~5~5!6~5~5~A&amp;f=51419626\
Accept-Language: zh-CN,zh;q=0.9\
Cookie: PHPSESSID=mhb9m4l0spcm39pb6pl2r82r40\
Range: bytes=98304-\
'

        }
    pkt_in(arg)
