# $language = "python"
# $interface = "1.0"

# 你要连接的ssh服务器ip
host = 'rhelp.fxdata.cn'
# ssh用户名
user = 'root'
# ssh密码
passwd = 'FxData!Cds@2016_'

import os, sys

varPath = os.path.abspath(__file__)
if varPath not in sys.path:
    sys.path.insert(0, varPath)
	
import get_cds_info


# f=open("rhelp.txt",'r')
# ssh_port=f.read()
def main():
    sn = "CAS0510000147"
    ssh_port = get_cds_info.get_cds_info(sn)
    if ssh_port is False:
        exit(0)
        cmd=" /SSH2 /L {0} /PASSWORD {1} /C 3DES /M MD5 {2} /P {3}".format(user, passwd, host, ssh_port)
        crt.Session.ConnectInTab(cmd)
        objTab = crt.GetActiveTab()
        objTab.Caption = ssh_port
        #crt.Dialog.MessageBox ("登陆成功","成功", 0 | 0)

main()