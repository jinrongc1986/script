# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# get Mail
# 打开邮箱并判断邮件获取邮件内容
# @author: liukelin  314566990@qq.com
# 
import os
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
import threading
import time
import sys
import re
import imp

imp.reload(sys)

dir_ = os.getcwd()

set_debuglevel = 0
pops = {'126.com': 'pop.126.com', '163.com': 'pop.163.com', 'qq.com': 'pop.qq.com', 'sina.com': 'pop.sina.com',
        'nbsky55.com': 'mail.nbsky55.com', 'loveyxx.com': 'mail.loveyxx.com','iloveyxx.com': 'mail.iloveyxx.com'}


#
# 获取邮件内容
# Email    账号
# password 密码
# limit    获取邮件数量
#
def get_mail(email, password, limit=1):
    pop3_server = ''
    st = email.split('@')[1]
    if st and (st in pops):
        pop3_server = pops[st]

    msgAll = []

    # 输入邮件地址, 口令和POP3服务器地址:
    email = email  # input('Email: ')
    password = password  # input('Password: ')
    pop3_server = pop3_server  # input('POP3 server: ') # pop.126.com   pop.163.com

    try:
        # 连接到POP3服务器:
        if ssl :
            server = poplib.POP3_SSL(pop3_server)
        else :
            server = poplib.POP3(pop3_server)

        # 可以打开或关闭调试信息:
        server.set_debuglevel(set_debuglevel)

        # 可选:打印POP3服务器的欢迎文字:
        # print(server.getwelcome().decode('utf-8'))

        # 身份认证:
        server.user(email)
        server.pass_(password)
    except:
        return msgAll

    # stat()返回邮件数量和占用空间:
    # print('Messages: %s. Size: %s' % server.stat())

    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()

    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    # print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)  # 总数

    page = (index - limit) if (index - limit) > 0 else 0
    for x in range(index, page, -1):  # 循环获取所有邮件

        try:
            resp, lines, octets = server.retr(x)

            # lines存储了邮件的原始文本的每一行,
            # 可以获得整个邮件的原始文本:
            msg_content = b'\r\n'.join(lines).decode('utf-8')

            # 稍后解析出邮件:
            msg = Parser().parsestr(msg_content)
            msgAll.append(print_info(msg, None))
        except:
            pass

    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()
    # except:
    # 	pass
    return msgAll


def get_mail_token(email, password, limit=1,ssl=True):
    pop3_server = ''
    st = email.split('@')[1]
    if st and (st in pops):
        pop3_server = pops[st]

    msgAll = []

    # 输入邮件地址, 口令和POP3服务器地址:
    email = email  # input('Email: ')
    password = password  # input('Password: ')
    pop3_server = pop3_server  # input('POP3 server: ') # pop.126.com   pop.163.com

    try:
        # 连接到POP3服务器:
        if ssl :
            server = poplib.POP3_SSL(pop3_server)
        else :
            server = poplib.POP3(pop3_server)

        # 可以打开或关闭调试信息:
        server.set_debuglevel(set_debuglevel)

        # 可选:打印POP3服务器的欢迎文字:
        print(server.getwelcome().decode('utf-8'))

        # 身份认证:
        server.user(email)
        server.pass_(password)
    except:
        print ('与邮件服务器连接失败，请检查账号密码及网络')
        return msgAll

    # stat()返回邮件数量和占用空间:
    # print('Messages: %s. Size: %s' % server.stat())

    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()

    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    # print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)  # 总数
    # print(index)

    page = (index - limit) if (index - limit) > 0 else 0
    # print(page)
    flag=True
    cnt=1
    token=[]
    while (flag and cnt <= 6 ) :
        time.sleep(5)
        for x in range(index, page, -1):  # 循环获取所有邮件
            try:
                resp, lines, octets = server.retr(x)
                # lines存储了邮件的原始文本的每一行,
                # 可以获得整个邮件的原始文本:
                messages = lines
                #print (messages)
                msg_content = b'\r\n'.join(lines).decode('utf-8')
                for message in messages :
                    if '(UTC)' in message.decode('utf-8') :
                        # print (message)
                        mailtime=message.decode('utf-8').split(';')[1]
                        # print (mailtime)
                        timeArray = time .strptime(mailtime, " %a, %d %b %Y %H:%M:%S %z (%Z)")
                        timemap = time.mktime(timeArray)
                        timenow = time.time()
                        difference = timenow - timemap
                        if difference < 60 :
                            print("成功获取最新的邮件，时间差值为：%.f" % difference)
                            flag = False
                            break
                        else :
                            flag = True
                            print ("没有最新时间的邮件，时间差值为：%.f" %difference)

                # 稍后解析出邮件:
                msg = Parser().parsestr(msg_content)
                msgAll.append(print_info(msg, None))
            except Exception as e:
                print (e)
            if not flag :
                for message in messages:
                    if 'x-ds-vetting-token' in message.decode('utf-8'):
                        # print (message)
                        token = message[-6:]
                        flag = False
                        # print(token.decode("utf-8"))
                        # token_new=str(token)[2:-1]
                        # print(token_new)
                        break
                if not flag :
                    break
                else :
                    print("此邮件中没有token")
                    continue
        if not flag :
            break
        else :
            print ("第%d次尝试获取token失败"%cnt)
            cnt += 1

    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()
    # except:
    #     pass
    # return msgAll
    return token


'''
只需要一行代码就可以把邮件内容解析为Message对象：

msg = Parser().parsestr(msg_content)
但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。

所以我们要递归地打印出Message对象的层次结构：
'''


# indent用于缩进显示:
def print_info(msg, data, indent=0):
    data = data if data else {}
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)

                    data['Subject'] = value  # 标题
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)

                    data[header] = {'name': name, 'addr': addr}  # 发送人、接收人
                    # print('%s%s: %s' % ('  ' * indent, header, value))

    # print(msg.is_multipart())
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            # print('%spart %s' % ('  ' * indent, n))
            # print('%s--------------------' % ('  ' * indent))
            print_info(part, data, indent + 1)
    else:
        # print('==' + content_type)
        # print(1)
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # 内容
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            data['content'] = content
            # print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            # 附件
            # print('%sAttachment: %s' % ('  ' * indent, content_type))
            data['attach'] = ''
        data['content_type'] = content_type
    return data


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


'''
decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。

文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
'''


def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# 检测是否有apple邮件
check = {}


def check_mail(threadNum, threadNo):
    file1 = 'mail.txt'  # 需要检测的文件
    file2 = 'check_mail.txt'  # 结果文件

    file = open("%s/%s" % (dir_, file1))
    l = 0

    # lines = file.readlines()
    # print("总行数:%s" % len(lines))
    # for l in range(0, len(lines)+1):
    while 1:
        line = file.readline()
        if not line:
            break
        l += 1
        print("=%s=%s=%s=" % (l, (l) % threadNum, threadNo))
        if (l - 1) % threadNum == threadNo:
            print("执行：%s" % l)

            # print("=%s=%s=" %(line.split('&')[0].strip(), line.split('&')[1].strip()))

            check[threadNo] = 0
            msg = get_mail(line.split('&')[0].strip(), line.split('&')[1].strip(), 100)
            for i in msg:
                if ('From' in i):
                    print(i['From']['addr'])
                    if i['From']['addr'] == 'appleid@id.apple.com':
                        check[threadNo] = 1
                        print("存在")
                        break
                else:
                    check[threadNo] = 1

            if check[threadNo] == 0:
                print("写入")
                f = open('%s/%s' % (dir_, file2), 'a')
                f.write(line)
                f.close()


'''
 提取apple邮件验证码
'''


def get_apple_code(mail, password, limit=10):
    '''
    <td class="paragraph verification-code" style="padding:0 5% 18px;font:300 23px/18px 'Lucida Grande', Lucida Sans, Lucida Sans Unicode, sans-serif, Arial, Helvetica, Verdana, sans-serif;color:#333;">575167</td>
    '''
    codes = []
    msg = get_mail(mail, password, limit)
    for i in msg:
        if ('From' in i):
            if i['From']['addr'] in ['appleid@id.apple.com']:
                if ('content' in i) and i['content']:
                    # print(i['content'])
                    try:
                        re_ = re.compile(r'<td class="paragraph verification-code".*?>(.*?)</td>', re.S)
                        code = re.findall(re_, i['content'])
                        if code and len(code) > 0:
                            codes.append(code[0])
                    except:
                        pass
    return codes


def check_start_mail(mailname, mailpasswd, depth=3):
    msg = get_mail(mailname, mailpasswd, depth)
    flag = False
    for i in range(0, depth + 1):
        try:
            subject = msg[i]["Subject"]
            # print(subject)
            # if subject=="欢迎使用 iCloud" or subject=="您的 Apple ID 被用于在 Web 浏览器上登录 iCloud":
            if subject == "欢迎使用 iCloud":
                flag = True
                return flag
        except:
            pass
    if flag == False:
        return flag

    '''
    # 总线程数 
    threadNum = 9

    threads = []
    for i in range(0, threadNum):
        t = threading.Thread( target=check_mail, name='check_mail', args=(threadNum, i) )
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print('all ok:%s' % time.strftime("%Y-%m-%d %H:%M:%S"))
    '''


if __name__ == "__main__":
    cnt = 0
    for i in range(10, 11):
        mailname = 'test0' + str(i) + '@loveyxx.com'
        mailpasswd = 'lslq9527'
        token = get_mail_token(mailname,mailpasswd, 2,ssl=True)
        print (token)
    #     # print (mailname)
    #     print(token.decode("utf-8"))
    #     flag = check_start_mail(mailname, mailpasswd, depth=2)
    #     if flag == False:
    #         print(mailname)
    #         cnt = cnt + 1
    # print('total error mail:%d' % cnt)

    # msg = get_mail("test1@loveyxx.com", "12345", 1)
    # subject = msg[0]["Subject"]
    # print(subject)






