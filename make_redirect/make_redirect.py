# -*- coding:utf-8 -*-
import os
from time import sleep
from xedge.tool import make_http_pcap


def create_bridge():
    os.system('brctl addbr br-xedge')
    os.system('ip l |grep veth0 || ip link add type veth')
    os.system('brctl addif br-xedge eth1')
    os.system('brctl addif br-xedge veth0')
    os.system('brctl setageing br-xedge 0')
    os.system('ifconfig br-xedge up')
    os.system('ifconfig veth0 up')
    os.system('ifconfig veth1 up')
    print("创建bridge成功")


def get_local_ip(nic='br100'):
    ip = os.popen((
                      "ifconfig %s | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1") % nic).read().split(
        '\n')[0]
    print("%s ip : %s" % (nic, ip))
    return ip


def tcprew(ip):
    iplist = ip.split('.')
    iplist[3] = str(int(iplist[3]) + 1)
    ipnew = '.'.join(iplist)
    os.system(
        'tcprewrite --srcipmap=%s:%s -i http_head.pcap -o bigFlows.pcap' % (
        ip, ipnew))
    os.system('rm -f http_head.pcap')
    print("重写 src_ip 为 : %s" % ipnew)


def tcprep(speed=1, loop=2):
    os.system(
        'tcpreplay -K -i veth1 --mbps %d  --loop %d  --unique-ip bigFlows.pcap' % (
        speed, loop))
    os.system('rm -f bigFlows.pcap')
    print("tcpreplay 执行成功，请确认重定向日志！")


def del_bridge():
    os.system('brctl delif br-xedge eth1')
    print("删除bridge 的 eth1成功")


def setbw(bw='1'):
    print("设置回源带宽为%sM，以防内网崩塌") % bw
    os.system(
        "/home/icache/configd config set download bandwidth work '%s'" % bw)
    print('设置非空闲时段成功')
    os.system(
        "/home/icache/configd config set download bandwidth spare '%s'" % bw)
    print('设置空闲时间成功')
    print('等待20秒，等icached恢复')
    sleep(20)


def main(flag='all'):
    # 制造所有资源的重定向为all,制造cnc_export重定向为cnc
    make_http_pcap.make_http_pcap(flag)
    create_bridge()
    br100_ip = get_local_ip(nic='br100')
    tcprew(br100_ip)
    tcprep(speed=1, loop=2)
    del_bridge()


if __name__ == '__main__':
    main(flag='all')
