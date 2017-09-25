import json,lianzhong_api
def get_yzm(driver,imgname):
    result='{"data": {"val": "FAA4", "id": 8631454506}, "result": true}'
    val=json.loads(result)["data"]["val"]
    print(val)
    return val


import requests
def get_out_ip(proxies):
    url = r'http://1212.ip138.com/ic.asp'
    r = requests.get(url,proxies=proxies)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('global ip:' + ip)
    return ip


import os
def router_init():
    # reconnect
    # restart
    cmd = 'python34 xiaomi.py 192.168.31.1 1qaz@3edcCJR reconnect'
    os.system(cmd)


if __name__=="__main__" :
    get_yzm(1,2)
    # router_init()
    # proxies = {'http': 'socks://192.168.0.61:1081','http': 'socks://192.168.0.61:1082', 'http':'socks://192.168.0.61:1083'}
    # for i in range(len(proxies)) :
    # get_out_ip(proxies)
