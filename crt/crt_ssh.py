# $language = "python"
# $interface = "1.0"

#你要连接的ssh服务器ip
host = 'rhelp.fxdata.cn'
#ssh用户名
user = 'root'
#ssh密码
passwd = 'FxData!Cds@2016_'

def main():
	port=None
	i=0
	while (port==None ):
		port=crt.Dialog.Prompt("请输入端口号","CDS设备ssh连接","",False)
		if not len(port)==5:
			port=None
			i+=1
		if i==2:
			crt.Dialog.MessageBox ("连续两次输入非法端口号","警告", 48 | 0)
			break
	else :
		cmd=" /SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s /P %s"%(user,passwd,host,port)
		crt.Session.ConnectInTab(cmd)
		#crt.Dialog.MessageBox ("登陆成功","成功", 0 | 0)

main()  