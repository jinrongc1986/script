#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
import re
def url_analysis(url):
    uri=url.split('//')[1].split('?')[0]
    try :
        query=url.split('//')[1].split('?')[1]
    except :
        pass
        #print ('no query')
    flag=True
    while flag :
        host=uri.split('/')[0]
        try :
            match = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", host)
            if match == [] :
                break
            uri=uri.split('/',1)[1]
        except Exception as e:
            flag=False
            print e
            pass
    dic={}
    host=uri.split('/',1)[0]
    path=uri.split('/')[1:-1]
    path_new='/'.join(path)
    filename=uri.split('/')[-1].split('.')[:-1]
    filename='.'.join(filename)
    extname=uri.split('/')[-1].split('.')[-1].strip()
    dic['host']=host
    dic['path']=path_new
    dic['filename']=filename
    dic['extname']=extname
    return dic

if __name__=='__main__':
    url='http://210.38.1.143:9999/175.6.224.12/cdn/qiyiapp/20170818/zip/1503047637.73_tpplaykernelhcdn.zip?dis_k=0a2de980428e06ee840cc18fbdee588cf&dis_t=1503244806&dis_dz=CT-GuangDong_GuangZhou&dis_st=36'
    print url_analysis(url)
    url='http://www.baidu.com/123.jpg'
    print url_analysis(url)
    
    
