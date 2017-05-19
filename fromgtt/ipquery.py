import collections
import requests
import json

s = requests.Session()


def get_city_taobao(ip):
    ip_service = 'http://ip.taobao.com/service/getIpInfo.php?ip='
    headers = {
        'user-agent': 'Mozilla/5.3 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.88 Safari/537.36'
    }
    while True:
        try:
            r = s.get(ip_service + ip, headers=headers, timeout=30)
            return r.json()['data']['city']
        except requests.exceptions.ReadTimeout:
            continue


def main():

    result = collections.defaultdict(lambda: 0)

    for line in file('ips.txt', 'r').readlines():
        count, ip = line.split()
        city = get_city_taobao(ip)
        if city:
            line = '%s %s' % (ip, city.encode('utf8'))
            print line
            result[city] += 1

    result_list = []
    for key, value in result.iteritems():
        result_list.append({'name': key, 'value': value})

    file('ip_result.txt', 'w').write(json.dumps(result_list))


if __name__ == '__main__':
    main()
