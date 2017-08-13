#coding=utf-8
import time
timestart=time.time()
timeend=time.time()
timecost=timeend-timestart
print (type(timecost))
print(("哈哈%f")%timecost)

username="xmxqb_600@nbsky55.com"
imgname=username.split('@')[0]
print (imgname)

result='{"data":{"val":"EVLW","id":8622908227},"result":true}'
val=result.split(":")[2].split(",")[0][1:-1]
print(val[0])