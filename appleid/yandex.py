# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep
import time
import get_mail
from urllib import request
import lianzhong_api
from user_agent import generate_user_agent
import json


# 一直等待某元素可见，默认超时10秒 locator 为XPATH 选择器
def is_visible(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutError:
        return False


# 一致等待某元素可见，默认超时10秒 LINK_TEXT 为XPATH 选择器
def is_visible_text(driver, text, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
        return True
    except TimeoutError:
        return False


# 一直等待某个元素消失，默认超时10秒 locator 为XPATH 选择器
def is_not_visible(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutError:
        return False


def get_yzm(driver, imgname):
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            imgurl = driver.find_element_by_xpath('//div[@class="form__field registration__captcha"]/div/div/img').get_attribute('src')
            success = True
        except:
            attempts += 1
            if attempts == 3:
                return False
            try:
                driver.find_element_by_xpath('//div[@class="captcha__reload"]').click()
            except:
                print('刷新验证码失败')
                return False
    try:
        request.urlretrieve(imgurl, imgname)
    except:
        print("获取验证码图片失败")
        return False
    try:
        result = lianzhong_api.main(file_name=imgname)
    except:
        print("获取验证码失败")
        return False
    if result == "":
        print ("联众api返回为空")
    else:
        print(result)
    return result


def double_check(driver, xpath, msg, method='XPATH'):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            if method == 'XPATH':
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                success = True
                return True
            elif method == 'LINK_TEXT':
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
                success = True
                return True
        except Exception as e:
            attempts += 1
            print(e)
            print(msg)
            if attempts == 3:
                return False
                # driver.close()
                # driver.quit()


def double_click_c(driver, xpath, msg, method='XPATH'):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            if method == 'XPATH':
                todo = WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                sleep(1)
                todo.click()
                success = True
                return True
            elif method == 'LINK_TEXT':
                todo = WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, xpath)))
                todo.click()
                success = True
                return True
            elif method == 'partialLinkText':
                todo = WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.partialLinkText, xpath)))
                todo.click()
                success = True
                return True
        except Exception as e:
            attempts += 1
            print(e)
            print(msg)
            if attempts == 2:
                return False
                # driver.close()
                # driver.quit()


def checkserver(driver):
    driver.switch_to.active_element
    xpath = "“iCloud” 已停止响应。"
    msg = "“iCloud” 已停止响应。"
    # flag = double_check(driver, xpath, msg, method='LINK_TEXT')
    try:
        WebDriverWait(driver, 2, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
        print(msg)
        driver.close()
        driver.quit()
        return 8
    except:
        pass
    xpath = "iCloud 尝试连接至服务器时出错。"
    msg = "iCloud 尝试连接至服务器时出错。"
    # flag = double_check(driver, xpath, msg, method='LINK_TEXT')
    try:
        WebDriverWait(driver, 2, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
        print(msg)
        driver.close()
        driver.quit()
        return 8
    except:
        pass


def checkunuse(driver, element_mail):
    element_cur = driver.switch_to.active_element
    msg = "无法使用此电子邮件地址。请选择其他电子邮件地址"
    # flag = double_check(driver, xpath, msg, method='LINK_TEXT')
    if element_mail == element_cur:
        print(msg)
        return False
    else:
        return True


def create_emailid(mailname, mailpasswd, body, proxy='', dttime=3):
    timestart = time.time()
    mailname = mailname
    mailpasswd = mailpasswd
    imgname = mailname.split('@')[0] + '.jpg'
    print("开始新一轮注册")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(mailname)
    ua = ""
    while ("Chrome" not in ua):
        ua = generate_user_agent()
    # print(ua)
    option = webdriver.ChromeOptions()
    option.add_argument('--user-agent=%s' % ua)
    if proxy:
        option.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(chrome_options=option)
    # driver=webdriver.Firefox()
    driver.get("https://mail.yandex.com/")

    # 获取网页
    # print(driver.get_cookies())
    # print(driver.current_window_handle)
    # print(driver.title)
    sleep(dttime)
    xpath = "Create account"
    msg = "点击创建账号失败"
    flag = double_click_c(driver, xpath, msg, method='LINK_TEXT')
    if not flag:
        driver.close()
        driver.quit()
        return 4
    # switch to frame
    try:
        cur_window = driver.current_window_handle
        driver.switch_to.window(cur_window)
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        return 4

    # 账号信息页面
    sleep(dttime)
    xpath = "//button[@type='submit']"
    msg = "等待激活按钮失败"
    flag = double_check(driver, xpath, msg, method='XPATH')
    if not flag:
        driver.close()
        driver.quit()
        return 4  # 网络超时
    try:
        # name
        print("start")
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(body['first_name'])
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(
            body['last_name'])
        # login
        driver.find_element_by_xpath("//input[@id='login']").send_keys(mailname)
        sleep(10)
        # password
        driver.find_element_by_xpath("//input[@id='password']").send_keys(mailpasswd)
        sleep(2)
        driver.find_element_by_xpath("//input[@id='password_confirm']").send_keys(mailpasswd)
        sleep(2)
        # 非手机认证
        xpath = "don't have"
        try:
            driver.find_element_by_xpath("//span[contains(text(), 't have')]").click()
        except:
            print ('fail')
            sleep(10)
            driver.find_element_by_xpath("//label[contains(text(), 't have')]").click()
        # driver.find_element_by_partial_link_text(xpath).click()
        # msg = "点击非手机认证失败"
        # flag = double_click_c(driver, xpath, msg, method='partialLinkText')
        # sleep (60)
        # if not flag:
        #     xpath="//span[@class='registration__pseudo-link link_has-no-phone']"
        #     msg = "点击非手机认证失败"
        #     flag = double_click_c(driver, xpath, msg, method='XPATH')
        #     print ("点击认证flag %s"%flag)
            # if not flag:
            #     driver.close()
            #     driver.quit()
            #     return 4
        # questions
        xpath = "//div[@class='human__confirm-wrapper']/div/div/span/button"
        msg = "等待安全问题选择失败"
        flag = double_check(driver, xpath, msg, method='XPATH')
        print (flag)
        # sleep (60)
        # if not flag:
        #     driver.close()
        #     driver.quit()
        #     return 4  # 网络超时
        driver.find_element_by_xpath("//input[@id='hint_answer']").send_keys(body['answer1'])
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        print("输入错误，关闭重来")
        return 4

    print("开始验证码自动识别")
    # 验证码自动化
    lianzhong_result = get_yzm(driver, imgname)
    if not lianzhong_result:
        driver.close()
        driver.quit()
        return 4
    try:
        val = json.loads(lianzhong_result)["data"]["val"]
    except:
        print("验证码格式返回错误")
        driver.close()
        driver.quit()
        return 4
    print(val)
    driver.find_element_by_xpath('//input[@id="captcha"  and @name="captcha"]').clear()
    driver.find_element_by_xpath('//input[@id="captcha"  and @name="captcha"]').send_keys(val)
    # 自动点击继续
    sleep(2 * dttime)
    # sleep(120)
    try:
        driver.find_element_by_xpath("//button[@type='submit']").click()
    except:
        print("已经人工点击注册？")
        pass

    print("注册成功")
    ###
    sleep(1)
    driver.close()
    driver.quit()
    timeend = time.time()
    timecost = timeend - timestart
    print(("本次耗时%.f秒") % timecost)
    print("等待10秒")
    sleep(10)
    return 1


if __name__ == '__main__':
    mailname_pre = 'cccc.xixihaha'
    domain = '@yandex.com'
    mailpasswd = 'Lslq9527'
    sn = 2
    proxy = "socks://127.0.0.1:1081"
    mailname = mailname_pre + str(sn).zfill(4)
    body = {'last_name': 'Mlqbll',
            'first_name': '贷',
            'answer1': 'chen'}
    create_emailid(mailname, mailpasswd, body, proxy)
