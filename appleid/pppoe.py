# coding=utf-8
from CloudId4 import create_cloudid
from time import sleep
import time
import requests
import socket
import os

def localIP():
    localIP = socket.gethostbyname(socket.gethostname())
    return localIP

def get_out_ip(proxy):
    url = r'http://1212.ip138.com/ic.asp'
    if not proxy:
        r = requests.get(url)
    else:
        proxies = proxy
        r = requests.get(url, proxies=proxies)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('global ip:' + ip)
    return ip

def router_init():
    # reconnect
    # restart
    cmd = 'python34 xiaomi.py 192.168.31.1 1qaz@3edcCJR reconnect'
    os.system(cmd)


def need_money(mailname_pre, domain, mailpasswd, body, count):
    ###############################参数设置######################################################
    timestart = time.time()
    okcnt = 0
    nokcnt = 0
    nokcnt_yzm = 0
    x = 0
    y = 0
    print('重启路由')
    # router_init()
    if localIP()=="30.30.32.2":
        proxies = [ 'socks://192.168.0.61:1086','socks://192.168.0.61:1087','socks://192.168.0.61:1088','socks://192.168.0.61:1089','socks://192.168.0.61:1090','socks://192.168.0.61:1091','socks://192.168.0.61:1092','socks://192.168.0.61:1094']
        # proxies = ['','socks://192.168.0.61:1081','socks://192.168.0.61:1083','socks://192.168.0.61:1084','socks://192.168.0.61:1085','socks://192.168.0.61:1093','socks://192.168.0.61:1095']
    else :
        proxies = ['']
        # proxies = ['socks://192.168.31.100:1095']
    for i in range(0, count):
        if x == 0 and y == 0:
            print("新的代理周期")
            # get_out_ip(proxy)
            lastround = time.time()
        if x == 5:
            print("次数已超过5次，切换代理/重启路由")
            x = 0
            y += 1
            router_init()
        if y == len(proxies):  # 总代理数量
            y = 0
            thisround = time.time()
            roundtime = thisround - lastround
            print("此次代理周期为%.f" % roundtime)
            timeleft = roundtime - 4000
            if timeleft < 0:
                print("代理周期结束，为确保代理可用，暂停%.f" % abs(timeleft))
                # sleep(abs(timeleft)-120)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                # print("120秒后重新开始")
                sleep(120)
            lastround = time.time()
        proxy = proxies[y]
        print(proxy)
        with open("%s.txt"%domain, "r") as f:  # 读取当前尝试id
            sn = f.readline()
        # 请设置邮箱信息
        # mailname = mailname_pre + sn.zfill(4) + domain
        mailname='test005@loveyxx.com'
        do = create_cloudid(mailname, mailpasswd, body, proxy)
        if do == 1:  # 顺利完成
            with open("%s.txt"%domain, "w") as f:
                sn = str(int(sn) + 1)
                f.write(sn)
            with open("result.txt", "a") as f:
                result = mailname + " PASS\n"
                f.write(result)
            okcnt += 1
        elif do == 2:  # 验证码3次失败
            with open("result.txt", "a") as f:
                result = mailname + " FAIL 验证码尝试多次失败\n"
                f.write(result)
            with open("%s.txt"%domain, "w") as f:  # 跳过此sn，开始下一个
                sn = str(int(sn) + 1)
                f.write(sn)
            nokcnt_yzm += 3
            if nokcnt_yzm > 18:
                break
        elif do == 3:  # 服务器报未知错误
            with open("result.txt", "a") as f:
                result = mailname + " FAIL server gg.....%s\n"%proxy
                f.write(result)
            nokcnt += 1
            print("切换代理并等待5分钟")
            router_init()
            sleep(300)
            y = y + 1
            x = 0
            # sleep(1800)
            # break #结束进程
        elif do == 4:  # 网络差，打不开网页
            with open("result.txt", "a") as f:
                result = mailname + " FAIL 网络超时\n"
                f.write(result)
            print("网络超时，等待10秒")
            sleep(10)
            nokcnt += 1
        elif do == 5:
            with open("%s.txt"%domain, "w") as f:
                sn = str(int(sn) + 1)
                f.write(sn)
            with open("result.txt", "a") as f:
                result = mailname + " FAIL 未点击开始使用\n"
                f.write(result)
            nokcnt += 1
        elif do == 6:
            with open("%s.txt"%domain, "w") as f:
                sn = str(int(sn) + 1)
                f.write(sn)
            with open("result.txt", "a") as f:
                result = mailname + " PASS\n"
                f.write(result)
            okcnt += 1
        elif do == 7:
            with open("%s.txt"%domain, "w") as f:
                sn = str(int(sn) + 1)
                f.write(sn)
            with open("result.txt", "a") as f:
                result = mailname + " FAIL 获取邮件token失败\n"
                f.write(result)
            nokcnt += 1
        x += 1

    timeend = time.time()
    timecost = timeend - timestart
    print(("总耗时%.f秒，总成功%d次，总失败%d次,验证码导致的失败%d次") % (timecost, okcnt, nokcnt, nokcnt_yzm))


if __name__ == '__main__':
    # mailname_pre='xmxqb_'
    # domain='@nbsky55.com'
    # mailpasswd='Xmx&qb3'
    mailname_pre = 'just'
    domain = '@loveyxx.com'
    mailpasswd = 'Lslq9527'
    body = {'last_name': 'Mlqbll',
            'first_name': '贷',
            'country': 'CHN',
            'birthday': '19880808',
            'password': '08ML15qb@',
            'question1': '130',
            'answer1': '三五河流',
            'question2': '137',
            'answer2': '王者荣耀',
            'question3': '143',
            'answer3': '东成西就'}
    count = 1000
    need_money(mailname_pre, domain, mailpasswd, body, count)
