#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = True

' This automatically generated script may need to be
' edited in order to work correctly.
Dim sn
Dim result
Dim md5
Sub CopyString(s)
    Set forms=WScript.CreateObject("forms.form.1")
    Set textbox=forms.Controls.Add("forms.textbox.1").Object
    With textbox
    .multiline=True
    .text=s
    .selstart=0
    .sellength=Len(.text)
    .copy
    End With
    End Sub

Sub Main
	crt.Screen.Synchronous = True
	crt.Screen.send("/home/icache/configd license show" + chr(13))
	crt.Screen.WaitForString("[root@")
	screenrow = crt.screen.CurrentRow - 1
	result=crt.Screen.Get(screenrow, 1, screenrow, 21 )	
	while (instr(result,"CAS") =0)
	screenrow = screenrow-1
	result=crt.Screen.Get(screenrow, 1, screenrow, 21 )
	wend
	sn=crt.Screen.Get(screenrow, 9, screenrow, 21 )
	crt.Screen.Send("#"+sn+chr(13))
	crt.Screen.Send("echo ""select md5('b15a8dad4b53dd14842f1892db1a9848"+sn+"')"" | mysql" + chr(13))
	crt.Screen.WaitForString("[root@")
	crt.Screen.WaitForString("[root@")
	screenrow = crt.screen.CurrentRow - 1
	md5=crt.Screen.Get(screenrow, 1, screenrow, 32 )
	'crt.Screen.Send("#"+md5+chr(13))
	crt.Screen.Synchronous = False
	End Sub
