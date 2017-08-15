import requests
import json
r = requests.get('http://127.0.0.1:8000/?types=0&count=10&country=国内&protocol=1')
ip_ports = json.loads(r.text)
print (ip_ports)
i=1
ip = ip_ports[i][0]
port = ip_ports[i][1]
proxies={
    'https':'https://%s:%s'%(ip,port)
}
print(proxies)
r = requests.get('https://www.icloud.com/',proxies=proxies)
r.encoding='utf-8'
#print (r.text)