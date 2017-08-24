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
            imgurl = driver.find_element_by_xpath('//idms-captcha/div/img[@alt="安全提示图片"]').get_attribute('src')
            success = True
        except:
            attempts += 1
            if attempts == 3:
                return False
            driver.find_element_by_xpath('//button[@class ="button link first"]').click()
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
        except Exception as e:
            attempts += 1
            print(e)
            print(msg)
            if attempts == 3:
                return False
                # driver.close()
                # driver.quit()


def create_cloudid(mailname, mailpasswd, body, proxy=''):
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
    driver.get("https://www.icloud.com/")

    # 获取网页
    # print(driver.get_cookies())
    # print(driver.current_window_handle)
    # print(driver.title)
    xpath = "现在创建一个。"
    msg = "点击创建账号失败"
    flag = double_click_c(driver, xpath, msg, method='LINK_TEXT')
    if not flag:
        driver.close()
        driver.quit()
        return 4
    # switch to frame
    try:
        switch_frame = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']/div[3]/div/iframe")))
        driver.switch_to.frame(switch_frame)
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        return 4

    # 账号信息页面
    xpath = "//security-answer[@answer-number='3']/div/input"
    msg = "等待安全提示问题3出现失败"
    flag = double_check(driver, xpath, msg, method='XPATH')
    if not flag:
        driver.close()
        driver.quit()
        return 4  # 网络超时
    try:
        # name
        print("start")
        driver.find_element_by_xpath("//last-name-input/div/input").send_keys(body['last_name'])
        driver.find_element_by_xpath("//first-name-input/div/input").send_keys(body['first_name'])
        # china select
        country_select = Select(driver.find_element_by_id('countryOptions'))
        country_select.select_by_value(body['country'])
        # birthday
        sleep(0.5)
        driver.find_element_by_xpath("//idms-error-wrapper/div/input").send_keys(body['birthday'])
        # email
        driver.find_element_by_xpath("//idms-error-wrapper/div/div/input").send_keys(mailname)
        # password
        driver.find_element_by_xpath("//password-input/input").send_keys(body['password'])
        driver.find_element_by_xpath("//confirm-password-input/div/input").send_keys(body['password'])
        # questions
        question1 = Select(driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set0 ']/security-question/div/div/select"))
        question1.select_by_value(body['question1'])
        driver.find_element_by_xpath("//security-answer[@answer-number='1']/div/input").send_keys(body['answer1'])
        question2 = Select(driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set1 ']/security-question/div/div/select"))
        question2.select_by_value(body['question2'])
        driver.find_element_by_xpath("//security-answer[@answer-number='2']/div/input").send_keys(body['answer2'])
        question3 = Select(driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set2 ']/security-question/div/div/select"))
        question3.select_by_value(body['question3'])
        driver.find_element_by_xpath("//security-answer[@answer-number='3']/div/input").send_keys(body['answer3'])
        # 将页面滚动条拖到底部
        driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').send_keys(Keys.TAB)
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
        return 4
    try:
        val = json.loads(lianzhong_result)["data"]["val"]
    except:
        print("验证码格式返回错误")
        return 4
    print(val)
    driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').clear()
    driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').send_keys(val)
    # 自动点击继续
    try:
        driver.find_element_by_xpath("//idms-toolbar/div/div/button").click()
    except:
        print("已经人工点击继续？？？")
        pass
    '''
    #手工验证模式
    print('第一次人工验证')
    sleep(15)
    #手工验证模式结束
    '''
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='char0']")))
            success = True
            if os.path.exists(imgname):
                os.remove(imgname)
                print('删除正常验证码', imgname)
            with open("dama.txt", "a") as f:
                timenow = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                damaok = ' PASS\n'
                f.write(timenow + damaok)
            print('发送邮件中。。。。等待30秒')
        except:
            # 上报错误的打码
            lianzhong_id = json.loads(lianzhong_result)["data"]["id"]
            lianzhong_api.report(lianzhong_id)
            attempts += 1
            if attempts == 3:
                driver.close()
                driver.quit()
                print("尝试验证码次数过多，即将此邮箱将被跳过")
                return 2  # 2表示图片验证尝试次数过多
            # if os.path.exists(imgname):
            #     os.rename(imgname, imgname.split('.')[0] + '_' + val + '.jpg')
            #     print("验证码失败")
            if os.path.exists(imgname):
                os.remove(imgname)
                print("删除无效验证码", imgname)
            with open("dama.txt", "a") as f:
                timenow = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                damanok = ' FAIL '
                f.write(timenow + damanok + val + '\n')
            # 验证码自动化
            lianzhong_result = get_yzm(driver, imgname)
            if not lianzhong_result:
                return 4
            try:
                val = json.loads(lianzhong_result)["data"]["val"]
            except:
                print("验证码格式返回错误")
                return 4
            print(val)
            driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').clear()
            driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').send_keys(val)
            # 点击继续
            try:
                driver.find_element_by_xpath("//idms-toolbar/div/div/button").click()
            except:
                print("已经人工点击继续？？？")
                pass
            '''
            # 手工验证模式
            print('第%d次人工验证'%(attempts+1))
            sleep(15)
            # 手工验证模式结束
            '''
    sleep(30)
    token = get_mail.get_mail_token(mailname, mailpasswd,1,ssl=True)
    token_new = token.decode("utf-8")
    print(token_new)
    # verification
    driver.find_element_by_xpath("//input[@id='char0']").send_keys(token_new[0])
    driver.find_element_by_xpath("//input[@id='char1']").send_keys(token_new[1])
    driver.find_element_by_xpath("//input[@id='char2']").send_keys(token_new[2])
    driver.find_element_by_xpath("//input[@id='char3']").send_keys(token_new[3])
    driver.find_element_by_xpath("//input[@id='char4']").send_keys(token_new[4])
    driver.find_element_by_xpath("//input[@id='char5']").send_keys(token_new[5])
    # 继续
    driver.find_element_by_xpath(
        "//step-verify-code/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/button[1]").click()
    # 服务器开始拒绝服务
    try:
        WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-popover/div/div/div/div')))
        print("gg...未知错误")
        driver.close()
        driver.quit()
        return 3  # 3表示服务器拒绝服务
    except:
        pass
    # 服务器超时
    try:
        WebDriverWait(driver, 10, 0.5).until_not(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='send-code']")))
    except:
        driver.close()
        driver.quit()
        print("页面未跳转")
        return 4  # 页面未跳转

    sleep(2)
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            # 同意条款1
            xpath = "//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]/label"
            msg = "等待同意1失败"
            flag = double_check(driver, xpath, msg)
            if not flag:
                sleep(2)
            msg = "点击同意1失败"
            flag = double_click_c(driver, xpath, msg)
            if not flag:
                try:
                    WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '//step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-popover/div/div/div/div')))
                    print("gg...未知错误")
                    driver.close()
                    driver.quit()
                    return 3  # 3表示服务器拒绝服务
                except:
                    pass
            print("同意条款1成功")

            # 同意条款2
            xpath = "//div[@role='alertdialog']/div/div/div[2]"
            msg = "等待同意2失败"
            flag = double_check(driver, xpath, msg)
            if not flag:
                sleep(2)
            msg = "点击同意2失败"
            flag = double_click_c(driver, xpath, msg)
            if not flag:
                # driver.close()
                # driver.quit()
                # return 5
                attempts += 1
            else:
                success = True
        except:
            driver.close()
            driver.quit()
            return 5

    print("同意条款2成功")

    # 开始使用iCloud
    xpath = "//div[@role='main']/div[2]"
    msg = "等待开始使用iCloud失败"
    flag = double_check(driver, xpath, msg)
    if not flag:
        sleep(2)
    msg = "点击开始使用iCloud失败"
    flag = double_click_c(driver, xpath, msg)
    if not flag:
        return 5
    print("点击开始使用iCloud成功")

    # 选择 设置与注销
    xpath = "//div[@title='iCloud 设置与注销']"
    msg = "等待点击设置失败"
    double_check(driver, xpath, msg)
    msg = "点击设置失败"
    flag = double_click_c(driver, xpath, msg)
    if not flag:
        driver.close()
        driver.quit()
        return 6
    # 注销
    xpath = "注销"
    msg = "等待注销失败"
    double_check(driver, xpath, msg, method='LINK_TEXT')
    msg = "注销失败"
    flag = double_click_c(driver, xpath, msg, method='LINK_TEXT')
    if not flag:
        driver.close()
        driver.quit()
        return 6
    print("注销成功")
    ###
    sleep(1)
    driver.close()
    driver.quit()
    timeend = time.time()
    timecost = timeend - timestart
    print(("本次耗时%.f秒") % timecost)
    return 1


if __name__ == '__main__':
    mailname = "xmxqb_382@nbsky55.com"
    mailpasswd = "Xmx&qb3"
    # proxy = '127.0.0.1:1081'
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
    # print (body['answer3'])
    create_cloudid(mailname, mailpasswd, body, proxy='')