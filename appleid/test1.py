import json,lianzhong_api
def get_yzm(driver,imgname):
    true=1
    result='{"data": {"val": "FAA4", "id": 8631454506}, "result": true}'
    val=json.loads(result)["data"]["val"]
    #val = result.split(":")[2].split(",")[0][1:-1]
    print(val)
    return val

get_yzm(1,2)

import requests
def get_out_ip():
    proxies={"http":"127.0.0.1:1081"}
    url = r'http://1212.ip138.com/ic.asp'
    r = requests.get(url,proxies=proxies)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip

get_out_ip()
