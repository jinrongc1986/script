import requests
import json
r = requests.get('http://127.0.0.1:8000/?types=0&count=10&country=国内')
ip_ports = json.loads(r.text)
print (ip_ports)
ip = ip_ports[0][0]
port = ip_ports[0][1]
proxies={
    'http':'http://%s:%s'%(ip,port),
    'https':'http://%s:%s'%(ip,port)
}
print(proxies)
r = requests.get('http://ip.chinaz.com/',proxies=proxies)
r.encoding='utf-8'
#print (r.text)