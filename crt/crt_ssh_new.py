# $language = "python"
# $interface = "1.0"

import os, sys
#varPath = os.path.abspath(__file__)
#if varPath not in sys.path:
#	sys.path.insert(0, varPath)

#import get_cds_info

################################################################
# 你要连接的ssh服务器ip
host = 'rhelp.fxdata.cn'
# ssh用户名
user = 'root'
# ssh密码
#passwd = 'FxData!Cds@2016_'
passwd = '123'


BASE_DIR = os.path.dirname(__file__)
filename=BASE_DIR+"\\rhelp.txt"

def judge(filename):
	if not os.path.exists(filename):
		crt.Dialog.MessageBox(filename + " not exist!")
		return 0
	else:
		return 1
def main(filename):
	if not judge(filename):
		return
	fp=file(filename,'r')
	ssh_port=fp.read()
	fp.close
	if ssh_port=="":
		alarm=str(filename) + "中ssh_port为空"
		crt.Dialog.MessageBox (alarm,"警告", 48 | 0)
		return
	else:
		cmd=" /SSH2 /L {0} /PASSWORD {1} /C 3DES /M MD5 {2} /P {3}".format(user, passwd, host, ssh_port)
		crt.Session.ConnectInTab(cmd)
		objTab = crt.GetActiveTab()
		objTab.Caption = ssh_port
		#crt.Dialog.MessageBox ("登陆成功","成功", 0 | 0)
main(filename)
