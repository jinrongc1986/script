# $language = "python"
# $interface = "1.0"
def main():
	sn=None
	i=0
	while (sn==None ):
		sn=crt.Dialog.Prompt("请输入CDS的sn号","web token计算","CAS0510000147",False)
		if 'CAS' not in sn:
			sn=None
			i+=1
		if i==2:
			crt.Dialog.MessageBox ("连续两次输入的sn号非法","警告", 48 | 0)
			break
	else :
		cmd=" echo \"select md5('b15a8dad4b53dd14842f1892db1a9848"+sn+"')\" | mysql"
		crt.Screen.Send(cmd + ' \r')
	#crt.Dialog.MessageBox ("请复制token","成功", 0 | 0)

main()  
#echo "select md5('b15a8dad4b53dd14842f1892db1a9848CAS0510000147')" | mysql
