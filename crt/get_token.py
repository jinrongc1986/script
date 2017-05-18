# $language = "python"
# $interface = "1.0"
def main():
    sn=crt.Dialog.Prompt("请输入CDS的sn号","web token计算","CAS0510000147",False)
    cmd=" echo \"select md5('b15a8dad4b53dd14842f1892db1a9848"+sn+"')\" | mysql"
    crt.Screen.Send(cmd + ' \r')
    #crt.Dialog.MessageBox ("密钥生成成功","请注意保密", 48 | 0)

main()  
#echo "select md5('b15a8dad4b53dd14842f1892db1a9848CAS0510000147')" | mysql
