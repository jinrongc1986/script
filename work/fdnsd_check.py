#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,commands,sys
data=open('/home/fdns/etc/match_cp_host/match_cp_host.conf','r')
t=json.load(data)
domains=[i['host'] for i in t['zones']]
failed=[]
noknum=0
success=[]
oknum=0
runnum=0
totalnum=len(domains)
for domain in domains:
	cmd='/home/fdns/sbin/fdnsd info '+domain
	output=commands.getoutput(cmd)
	if "tag mask[fb|b|w]: 0|0|1" in output:
		success.append(domain)
		oknum+=1
	else:
		failed.append(domain)
		noknum+=1
	runnum+=1
	percent=1.0*runnum/totalnum*100
	sys.stdout.write('\rcomplete percent:%10.4s%s'%(str(percent),'%'))
	sys.stdout.flush()
print "domain can be redirected :"
print success
print "domain can't be redirected :"
print failed
print "total domain counter is %d"%(oknum+noknum)
print "domain can be redirected : %d"%oknum
print "domain can't be redirected : %d"%noknum
