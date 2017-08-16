#coding=utf-8
from CloudId3 import create_cloudid
from time import sleep
import time
import requests

def get_out_ip(proxies):
    url = r'http://1212.ip138.com/ic.asp'
    if not proxies:
        r = requests.get(url)
    else :
        proxies={"http":"127.0.0.1:1081"}
        r = requests.get(url,proxies=proxies)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip

###############################参数设置######################################################
timestart=time.time()
okcnt=0
nokcnt=0
nokcnt_yzm=0
# proxy='127.0.0.1:1081'
proxy='socks://192.168.0.61:1080'
# proxy=''
# proxies = proxy
# get_out_ip(proxies)
with open("mail.txt", "r") as f:  # 读取开始尝试id
    sn = f.readline()
mailstart = "xmxqb_" + sn + "@nbsky55.com"

for i in range(0,1000):
    if int(sn)==780:
        break
    with open("mail.txt", "r") as f: #读取当前尝试id
        sn = f.readline()
    # 请设置邮箱信息
    mailname = "xmxqb_" + sn + "@nbsky55.com"
    mailpasswd = "Xmx&qb3"
    a = create_cloudid(mailname,mailpasswd,proxy)
    if a == 1:  #顺利完成
        with open("mail.txt","w") as f:
            sn = str(int(sn)+1)
            f.write(sn)
        with open("result.txt","a") as f:
            result = mailname + " PASS\n"
            f.write(result)
        okcnt += 1
    elif a == 2: #验证码3次失败
        with open("result.txt","a") as f:
            result = mailname + " FAIL 验证码尝试多次失败\n"
            f.write(result)
        with open("mail.txt","w") as f: #跳过此sn，开始下一个
            sn = str(int(sn)+1)
            f.write(sn)
        nokcnt_yzm += 3
        if  nokcnt_yzm > 18 :
            break
    elif a == 3: #服务器报未知错误
        with open("result.txt","a") as f:
            result = mailname + " FAIL server gg.....\n"
            f.write(result)
        nokcnt += 1
        print("间隔1800秒")
        sleep(1800)
        #break #结束进程
    elif a == 4: #网络差，打不开网页
        with open("result.txt","a") as f:
            result = mailname + " FAIL 网络超时\n"
            f.write(result)
        print("网络超时，等待60秒")
        sleep(60)
        nokcnt += 1
    elif a == 5:
        with open("mail.txt","w") as f:
            sn = str(int(sn)+1)
            f.write(sn)
        with open("result.txt","a") as f:
            result = mailname + " FAIL 未点击开始\n"
            f.write(result)
        nokcnt += 1
timeend = time.time()
timecost = timeend - timestart
print(("总耗时%.f秒，总成功%d次，总失败%d次,验证码导致的失败%d次") % (timecost,okcnt,nokcnt,nokcnt_yzm))