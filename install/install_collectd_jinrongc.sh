#!/bin/bash
set -x

CONF="/etc/collectd.conf"
TMP='/tmp/collectd'


## Get SN from this device.

hostname=`/home/icache/configd license show|grep sn | awk -F\" '{print $4}'`
if [ -z $hostname ]; then
    # No icache lisense, using dmi product_id
    hostname=`hostname`
    # hostname=`cat /sys/class/dmi/id/product_uuid  |awk -F'-' '{print $5}'`

fi


echo "Hostname: $hostname"

mkdir $TMP
pushd $TMP

echo 'Downloading rpms'
wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/collectd-5.5.0-1.el6.x86_64.rpm
wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/collectd-disk-5.5.0-1.el6.x86_64.rpm
wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/collectd-virt-5.5.0-1.el6.x86_64.rpm
wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/collectd-write_http-5.5.0-1.el6.x86_64.rpm
wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/collectd-nginx-5.5.0-1.el6.x86_64.rpm
wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/collectd.conf.tpl
wget ftp://192.168.1.222/test/collectd.conf.jinrongc

echo 'Install collectd...'
yum localinstall collectd*.rpm -y


echo 'Config collectd...'
#####cp collectd.conf.tpl $CONF
cp  collectd.conf.jinrongc $CONF
sed -i s/FX_HOSTNAME/$hostname/g $CONF

###CONFD="/etc/collectd.conf.d/"
###mkdir -p $CONFD
###wget --user fxdata --password Fxdata@CDS2000 http://www.fxdata.cn:8001/xvirt/collectd/check_f2cdn.py
###mv check_f2cdn.py $CONFD
###chmod +x $CONFD/check_f2cdn.py
###chmod +r /home/f2cdn/check_info.log


popd
rm -r $TMP

echo 'Start collectd...'
chkconfig collectd on
/etc/init.d/collectd restart

sleep 3

tail /var/log/collectd.log

echo '==============================='
echo 'collectd installed successfully..'
echo '==============================='

