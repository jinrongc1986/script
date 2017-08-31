# -*- coding:utf-8 -*-
import os, subprocess
from time import sleep
import make_http_pcap


def create_bridge_old():
    path = os.path.split(os.path.realpath(__file__))[0]
    cmd = 'bash %s/start_mirror.sh' % path
    cb = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    cb.communicate()
    print ("创建bridge成功")


def create_bridge():
    os.system('brctl addbr br-xedge')
    os.system('ip l |grep veth0 || ip link add type veth')
    os.system('brctl addif br-xedge eth1')
    os.system('brctl addif br-xedge veth0')
    os.system('brctl setageing br-xedge 0')
    os.system('ifconfig br-xedge up')
    os.system('ifconfig veth0 up')
    os.system('ifconfig veth1 up')
    print ("创建bridge成功")


def get_local_ip(nic='br100'):
    ip = os.popen((
                  "ifconfig %s | grep 'inet addr:' | grep -v '127.0.0.1' | \
                  cut -d: -f2 | awk '{print $1}' | head -1")
                  % nic).read().split(
        '\n')[0]
    print ("%s ip : %s" % (nic, ip))
    return ip


def tcprew(ip):
    iplist = ip.split('.')
    iplist[3] = str(int(iplist[3]) + 1)
    ipnew = '.'.join(iplist)
    cmd = 'tcprewrite --srcipmap=%s:%s -i http_head.pcap -o bigFlows.pcap' % (
    ip, ipnew)
    tcprw = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    tcprw.communicate()
    print ("重写 src_ip 为 : %s" % ipnew)


def tcprep(speed=1, loop=2):
    cmd = 'tcpreplay -K -i veth1 --mbps %d  --loop %d  \
            --unique-ip bigFlows.pcap' % (
    speed, loop)
    tcprp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    tcprp.communicate()
    print ("tcpreplay 执行成功，请确认回源队列！")


def del_bridge():
    cmd = 'brctl delif br-xedge eth1'
    del_br = subprocess.call(cmd, shell=True)
    print ("清除bridge成功")


def setbw(bw='1'):
    print("设置回源带宽为%sM，以防内网崩塌") % bw
    cmd1 = "/home/icache/configd config set download bandwidth work '%s'" % bw
    cmd2 = "/home/icache/configd config set download bandwidth spare '%s'" % bw
    setbw1 = subprocess.call(cmd1, shell=True)
    print ('设置非空闲时段成功')
    setbw2 = subprocess.call(cmd2, shell=True)
    print ('设置空闲时间成功')
    print ('等待20秒，等icached恢复')
    sleep(20)


def main(flag='all'):
    # 制造所有资源的重定向为all,制造cnc_export重定向为cnc
    setbw(bw="1")
    make_http_pcap.make_http_pcap(flag)
    create_bridge()
    br100_ip = get_local_ip(nic='br100')
    tcprew(br100_ip)
    tcprep(speed=1, loop=2)
    del_bridge()


if __name__ == '__main__':
    main()
