#!/bin/bash
# 此脚本用 tcpreplay 将 pcap 包重放到镜像网卡上。
# 实现原理是：创建一对虚拟网卡和一个网桥, 将虚拟网卡的一端插入网桥，另外一端
# 加到网桥中，然后 tcpreplay 往另外一个虚拟网卡发送包。

br="br-xedge"
brctl addbr $br

ip l |grep veth0 || ip link add type veth
brctl addif $br eth1
brctl addif $br veth0
brctl setageing $br 0

ifconfig $br up
ifconfig veth0 up
ifconfig veth1 up

echo ''
echo ''
echo "ok, please run below command to bring up mirror traffic"
echo "$ tcpreplay -K -i veth1 --mbps 50  --loop 100  --unique-ip bigFlows.pcap"

