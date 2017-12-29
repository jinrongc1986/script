#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-  
import sys
import datetime

def swtime(timeStamp):
    timeStamp=int(timeStamp)
    # timeArray = datetime.datetime.utcfromtimestamp(timeStamp)
    timeArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    print otherStyleTime

if __name__ == "__main__":
    try:
        timeStamp=sys.argv[1]
        swtime(timeStamp)
    except Exception as e:
        print ("need argv: timeStamp")
