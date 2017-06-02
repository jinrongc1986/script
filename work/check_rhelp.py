import os,time
cmd=""" echo "select rhelp from ordoac.feedback where sn='CAS0510000147'" | mysql -h 192.168.1.12 -uselector -pfxdata_Select-2016 -P 3305"""
while (True):
    output=os.popen(cmd).readlines()
    print output
    if "56601:58250:51259" not in output[-1]:
        print "rhelp port changed"
        break
    print time.strftime('%H:%M:%S',time.localtime(time.time()))
    time.sleep(10)

