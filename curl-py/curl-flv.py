#-*- coding:utf-8 -*-
import os,subprocess,time
cmd="curl -o /dev/null -L 'http://183.136.235.145/videos/v0/20160913/91/e9/2d2f863268d57acb443cf8cddcbbc503.f4v?key=03d845c5bd16e4b9e8e1c32cdbb050863&dis_k=04b886f48730b6ea574111751cd62ec9&dis_t=1487661174&src=iqiyi.com&qyid=&qypid=&la=CT|ZheJiang_HangZhou&li=quzhou2_ct&lsp=0&lc=63&uuid=73c3a8a0-58abe876-b5'   --user-agent '"
for i in range(1,1000):
    cmd1=cmd+str(i)+"'"
    p = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(30)
