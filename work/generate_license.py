# -*- coding:utf-8 -*-
import random

def generate_licence(num):
    """
    生成num位字母和数字的随机字符串
    :param num: 生成字符串位数
    :return: string
    """
    s = ""
    for i in range(num):
        n = random.randint(1, 2)    # n=1生成数字, n=2生成字母
        if n == 1:
            s += str(random.randint(0, 9))
        else:
            s += chr(96 + random.randint(1, 26))

    return s

print (generate_licence(16))
