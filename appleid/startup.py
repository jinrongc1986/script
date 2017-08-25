# coding=utf-8
from CloudId4 import create_cloudid
from time import sleep
import time
import requests


def get_out_ip(proxies):
    url = r'http://1212.ip138.com/ic.asp'
    if not proxies:
        r = requests.get(url)
    else:
        proxies = {"http": "127.0.0.1:1081"}
        r = requests.get(url, proxies=proxies)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip


def need_money(mailname_pre, domain, mailpasswd, body, count):
    ###############################参数设置######################################################
    timestart = time.time()
    okcnt = 0
    nokcnt = 0
    nokcnt_yzm = 0
    # proxy='127.0.0.1:1081'
    # proxy='socks://192.168.0.61:1080'
    proxies = ['', 'socks://192.168.31.100:1082', 'socks://192.168.31.100:1082', 'socks://192.168.31.100:1085']
    # get_out_ip(proxies)
    with open("mail.txt", "r") as f:  # 读取开始尝试id
        sn = f.readline()
    # mailstart = mailname_pre + sn + domain
    # print ("mailstart")
    x = 0
    y = 0
    for i in range(0, count):
        if x == 0 and y == 0:
            print("新的代理周期")
            lastround = time.time()
        if x == 5:
            print("次数已超过5次")
            x = 0
            y += 1
        if y == len(proxies):  # 总代理数量
            y = 0
            thisround = time.time()
            roundtime = thisround - lastround
            print("此次代理周期为%.f" % roundtime)
            timeleft = roundtime - 3600
            if timeleft < 0:
                print("代理周期结束，为确保代理可用，暂停%.f" % abs(timeleft))
                sleep(abs(timeleft))
        proxy = proxies[y]
        print(proxy)
        with open("mail.txt", "r") as f:  # 读取当前尝试id
            sn = f.readline()
        # 请设置邮箱信息
        mailname = mailname_pre + sn + domain
        do = create_cloudid(mailname, mailpasswd, body, proxy)
        if do == 1:  # 顺利完成
            with open("mail.txt", "w") as f:
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
            with open("mail.txt", "w") as f:  # 跳过此sn，开始下一个
                sn = str(int(sn) + 1)
                f.write(sn)
            nokcnt_yzm += 3
            if nokcnt_yzm > 18:
                break
        elif do == 3:  # 服务器报未知错误
            with open("result.txt", "a") as f:
                result = mailname + " FAIL server gg.....\n"
                f.write(result)
            nokcnt += 1
            print("切换代理")
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
            with open("mail.txt", "w") as f:
                sn = str(int(sn) + 1)
                f.write(sn)
            with open("result.txt", "a") as f:
                result = mailname + " FAIL 未点击开始使用\n"
                f.write(result)
            nokcnt += 1
        elif do == 6:
            with open("mail.txt", "w") as f:
                sn = str(int(sn) + 1)
                f.write(sn)
            with open("result.txt", "a") as f:
                result = mailname + " PASS\n"
                f.write(result)
            okcnt += 1
        elif do == 7:
            with open("mail.txt", "w") as f:
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
    mailname_pre = 'test0'
    domain = '@loveyxx.com'
    mailpasswd = 'lslq9527'
    body = {'last_name': 'Zrcredit',
            'first_name': '贷',
            'country': 'CHN',
            'birthday': '19891212',
            'password': '21B12a5&',
            'question1': '130',
            'answer1': '第一财经',
            'question2': '137',
            'answer2': '万华化学',
            'question3': '143',
            'answer3': '三聚环保'}
    count = 100
    need_money(mailname_pre, domain, mailpasswd, body, count)
