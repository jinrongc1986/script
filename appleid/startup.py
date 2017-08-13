#coding=utf-8
from CloudId2 import create_cloudid

for i in range(0,5):
    with open("mail.txt", "r") as f: #读取当前尝试id
        sn = f.readline()
    # 请设置邮箱信息
    mailname = "xmxqb_" + sn + "@nbsky55.com"
    mailpasswd = "Xmx&qb3"
    a = create_cloudid(mailname,mailpasswd)
    if a == 1:
        with open("mail.txt","w") as f:
            sn = str(int(sn)+1)
            f.write(sn)
        with open("result.txt","a") as f:
            result = mailname + " PASS\n"
            f.write(result)
    elif a == 2:
        with open("result.txt","a") as f:
            result = mailname + " FAIL\n"
            f.write(result)
        with open("mail.txt","w") as f: #跳过此sn，开始下一个
            sn = str(int(sn)+1)
            f.write(sn)
    elif a == 3:
        with open("result.txt","a") as f:
            result = mailname + " FAIL server gg.....\n"
            f.write(result)
        break #结束进程


#a = create_cloudid(mailname, mailpasswd)

