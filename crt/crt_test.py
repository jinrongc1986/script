# $language = "python"
# $interface = "1.0"
def main():
	filepath=crt.Dialog.FileOpenDialog("请选择一个文件" , "打开" , "" , filter = "|.py" )  #Log Files (*.log)|*.log
	crt.Dialog.MessageBox(filepath,"路径",64|0)
	crt.Screen.Send('#'+filepath + ' \r')
	for i in range(101,105):
		x="CAS0510000" + str(i)
		crt.Screen.Send('#'+ x + ' \r')
		crt.Screen.WaitForString("not exist",5)
		#crt.Screen.WaitForString("root")
#if __name__=="__main__":
main()