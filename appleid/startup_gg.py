#coding=utf-8
import os
import re

sn=613
mailname = "xmxqb_"+str(sn)+"@nbsky55.com"
print(mailname)
mailpasswd = "Xmx&qb3"
a=0
if a==0:
    with open("startup.py","rb+") as f:
        save_list=f.readlines()
    for num,line in enumerate(save_list):
        if "sn=" in str(line):
            snnow = str(line).split("=")[1].split("\\r")[0]
            snnew = str(int(snnow)+1)
            snnow = bytes(snnow,encoding='utf-8')
            snnew = bytes(snnew, encoding='utf-8')
            line = re.sub(snnow, snnew, line)
            save_list[num] = line
            break
    with open("startup.py", "w") as f:
        for line in save_list:
            f.write(str(line)[2:-5]+'\n')

#a = create_cloudid(mailname, mailpasswd)

