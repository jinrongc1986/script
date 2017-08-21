import requests
import json
r = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=aa7d41b7a281a52c14c43e76fc4ac7a1&sep=3')
proxyinfo=r.text.split("\n")[0]
ip=proxyinfo.split(":")[0]
port=proxyinfo.split(":")[1]
proxies={
    'https':'https://%s:%s'%(ip,port)
}
print(proxies)
r = requests.get('https://www.baidu.com/',proxies=proxies,timeout=2)
r.encoding='utf-8'
print (r.text)