#coding=utf-8
from CloudId import create_cloudid
from time import sleep
import time
def need_money(mailname_pre,domain,mailpasswd,body,count):
    timestart=time.time()
    okcnt=0
    nokcnt=0
    nokcnt_yzm=0
    with open("mail.txt", "r") as f:  # 读取开始尝试id
        sn = f.readline()
    # mailstart = "xmxqb_" + sn + "@nbsky55.com"

    for i in range(0,count):
        with open("mail.txt", "r") as f: #读取当前尝试id
            sn = f.readline()
        # 请设置邮箱信息
        mailname = domain + sn + domain
        a = create_cloudid(mailname,mailpasswd)
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
            sleep(1200)
            #break #结束进程
        elif a == 4: #网络差，打不开网页
            with open("result.txt","a") as f:
                result = mailname + " FAIL 网络超时\n"
                f.write(result)
            sleep(60)
            nokcnt += 1
    timeend = time.time()
    timecost = timeend - timestart
    print(("总耗时%.f秒，总成功%d次，总失败%d次,验证码导致的失败%d次") % (timecost,okcnt,nokcnt,nokcnt_yzm))

if __name__=='__main__':
    mailname_pre='xmxqb_'
    domain='@nbsky55.com'
    mailpasswd='Xmx&qb3'
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
            'answer3': u'三聚环保'}
    count = 100
    need_money(mailname_pre,domain,mailpasswd,body,count)