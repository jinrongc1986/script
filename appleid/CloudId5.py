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
import showapi
import lianzhong_api
from user_agent import generate_user_agent
import pdb
import json


# 一直等待某元素可见，默认超时10秒 locator 为XPATH 选择器
def is_visible(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutError:
        return False


# 一致等待某元素可见，默认超时10秒 LINK_TEXT 为XPATH 选择器
def is_visible_text(driver, text, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.LINK_TEXT, text)))
        return True
    except TimeoutError:
        return False


# 一直等待某个元素消失，默认超时10秒 locator 为XPATH 选择器
def is_not_visible(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until_not(
            EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutError:
        return False


def get_yzm(driver, imgname):
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            imgurl = driver.find_element_by_xpath(
                '//idms-captcha/div/img[@alt="安全提示图片"]').get_attribute('src')
            success = True
        except:
            attempts += 1
            if attempts == 3:
                return False
            try:
                driver.find_element_by_xpath(
                    '//button[@class ="button link first"]').click()
            except:
                print('刷新验证码失败')
                return False
    try:
        request.urlretrieve(imgurl, imgname)
        url = imgurl.split(',')[1]
        result = showapi.main(url)
    except:
        print("获取验证码失败")
        return False
    if result == "":
        print("验证码api返回为空")
    else:
        print(result)
    return result


def double_check(driver, xpath, msg, method='XPATH'):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            if method == 'XPATH':
                WebDriverWait(driver, 10, 0.5).until(
                    EC.visibility_of_element_located((By.XPATH, xpath)))
                success = True
                return True
            elif method == 'LINK_TEXT':
                WebDriverWait(driver, 10, 0.5).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
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
                todo = WebDriverWait(driver, 10, 0.5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath)))
                sleep(1)
                todo.click()
                success = True
                return True
            elif method == 'LINK_TEXT':
                todo = WebDriverWait(driver, 10, 0.5).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, xpath)))
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
        WebDriverWait(driver, 2, 0.5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
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
        WebDriverWait(driver, 2, 0.5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
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


def create_cloudid(mailname, mailpasswd, body, proxy='', dttime=5):
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
    sleep(dttime)
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
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='dialog']/div[3]/div/iframe")))
        driver.switch_to.frame(switch_frame)
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        return 4

    # 账号信息页面
    sleep(dttime)
    xpath = "//security-answer[@answer-number='3']/div/idms-error-wrapper/div/input"
    msg = "等待安全提示问题3出现失败"
    flag = double_check(driver, xpath, msg, method='XPATH')
    if not flag:
        driver.close()
        driver.quit()
        return 4  # 网络超时
    try:
        # name
        print("start")
        driver.find_element_by_xpath(
            "//last-name-input/div/idms-error-wrapper/div/input").send_keys(
            body['last_name'])
        driver.find_element_by_xpath(
            "//first-name-input/div/idms-error-wrapper/div/input").send_keys(
            body['first_name'])
        # china select
        country_select = Select(driver.find_element_by_id('countryOptions'))
        country_select.select_by_value(body['country'])
        # birthday
        sleep(0.5)
        driver.find_element_by_xpath(
            "//date/idms-error-wrapper/div/input").send_keys(body['birthday'])
        # email
        element_mail = driver.find_element_by_xpath(
            "//email-input/idms-error-wrapper/div/div/input")
        driver.find_element_by_xpath(
            "//email-input/idms-error-wrapper/div/div/input").send_keys(
            mailname)
        # password
        driver.find_element_by_xpath("//password-input/div/input").send_keys(
            body['password'])
        driver.find_element_by_xpath(
            "//confirm-password-input/div/idms-error-wrapper/div/input").send_keys(
            body['password'])
        # questions
        question1 = Select(driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set0 ']/security-question/div/div/select"))
        question1.select_by_value(body['question1'])
        driver.find_element_by_xpath(
            "//security-answer[@answer-number='1']/div/idms-error-wrapper/div/input").send_keys(
            body['answer1'])
        question2 = Select(driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set1 ']/security-question/div/div/select"))
        question2.select_by_value(body['question2'])
        driver.find_element_by_xpath(
            "//security-answer[@answer-number='2']/div/idms-error-wrapper/div/input").send_keys(
            body['answer2'])
        question3 = Select(driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set2 ']/security-question/div/div/select"))
        question3.select_by_value(body['question3'])
        driver.find_element_by_xpath(
            "//security-answer[@answer-number='3']/div/idms-error-wrapper/div/input").send_keys(
            body['answer3'])
        # 截图密保
        '''
        target = driver.find_element_by_xpath(
            "//div[@class='form-group qa-container qa-set0 ']/security-question/div/div/select")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        driver.get_screenshot_as_file("%s.png" % mailname)
        '''
        # 将页面滚动条拖到底部
        driver.find_element_by_xpath(
            '//captcha-input/div/idms-error-wrapper/div/input[@id="captcha-input"]').send_keys(
            Keys.TAB)
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
        # val = json.loads(lianzhong_result)["data"]["val"]
        val = lianzhong_result
    except:
        print("验证码格式返回错误")
        driver.close()
        driver.quit()
        return 4
    driver.find_element_by_xpath(
        '//captcha-input/div/idms-error-wrapper/div/input[@id="captcha-input"]').clear()
    driver.find_element_by_xpath(
        '//captcha-input/div/idms-error-wrapper/div/input[@id="captcha-input"]').send_keys(
        val)
    # 自动点击继续
    sleep(dttime)
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
            WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(
                (By.XPATH, "//input[@id='char0']")))
            success = True
            if os.path.exists(imgname):
                os.remove(imgname)
                print('删除正常验证码', imgname)
            with open("dama.txt", "a") as f:
                timenow = (
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                damaok = ' PASS\n'
                f.write(timenow + damaok)
            print('发送邮件中。。。。等待5秒')
        except:
            # 检查是否邮箱已经使用
            if not checkunuse(driver, element_mail):
                driver.close()
                driver.quit()
                return 9
            checkserver(driver)
            # 上报错误的打码
            # lianzhong_id = json.loads(lianzhong_result)["data"]["id"]
            # lianzhong_api.report(lianzhong_id)
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
                timenow = (
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                damanok = ' FAIL '
                f.write(timenow + damanok + val + '\n')
            # 验证码自动化
            lianzhong_result = get_yzm(driver, imgname)
            if not lianzhong_result:
                return 4
            try:
                # val = json.loads(lianzhong_result)["data"]["val"]
                val = lianzhong_result
            except:
                print("验证码格式返回错误")
                return 4
            driver.find_element_by_xpath(
                '//captcha-input/div/idms-error-wrapper/div/input[@id="captcha-input"]').clear()
            driver.find_element_by_xpath(
                '//captcha-input/div/idms-error-wrapper/div/input[@id="captcha-input"]').send_keys(
                val)
            # 点击继续
            try:
                driver.find_element_by_xpath(
                    "//idms-toolbar/div/div/button").click()
            except:
                print("已经人工点击继续？？？")
                pass
            '''
            # 手工验证模式
            print('第%d次人工验证'%(attempts+1))
            sleep(15)
            # 手工验证模式结束
            '''
    # sleep(30)
    token = get_mail.get_mail_token(mailname, mailpasswd, 1, ssl=True)
    if token == []:
        print("邮件获取失败")
        return 7
    token_new = token.decode("utf-8")
    print(token_new)
    # verification
    driver.find_element_by_xpath("//input[@id='char0']").send_keys(
        token_new[0])
    driver.find_element_by_xpath("//input[@id='char1']").send_keys(
        token_new[1])
    driver.find_element_by_xpath("//input[@id='char2']").send_keys(
        token_new[2])
    driver.find_element_by_xpath("//input[@id='char3']").send_keys(
        token_new[3])
    driver.find_element_by_xpath("//input[@id='char4']").send_keys(
        token_new[4])
    driver.find_element_by_xpath("//input[@id='char5']").send_keys(
        token_new[5])
    # 继续
    driver.find_element_by_xpath(
        "//step-verify-code/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/button[1]").click()
    # 服务器开始拒绝服务
    try:
        # WebDriverWait(driver, 2, 0.5).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     '//step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-error-wrapper/div/idms-error/div/div/span')))

        xpath = "//security-code/div/idms-error-wrapper\
                /div/idms-error/div/div/span"
        WebDriverWait(driver, 2, 0.5).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
        print("gg...未知错误")
        driver.close()
        driver.quit()
        return 3  # 3表示服务器拒绝服务
    except:
        pass
    # 服务器超时
    try:
        WebDriverWait(driver, 10, 0.5).until_not(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@id='send-code']")))
    except:
        sleep(5)
        try:
            xpath = "//security-code/div/idms-error-wrapper\
                            /div/idms-error/div/div/span"
            WebDriverWait(driver, 2, 0.5).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            print("gg...未知错误")
            driver.close()
            driver.quit()
            return 3  # 3表示服务器拒绝服务
        except:
            pass
        # 服务器超时
        print("页面未跳转")
        # pdb.set_trace()
        driver.close()
        driver.quit()
        return 8  # 页面未跳转

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
                    xpath = "//security-code/div/idms-error-wrapper\
                                    /div/idms-error/div/div/span"
                    WebDriverWait(driver, 2, 0.5).until(
                        EC.presence_of_element_located((By.XPATH, xpath)))
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

    # 确认服务器是否停止响应
    checkserver(driver)

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
    print("等待%d秒" % dttime)
    sleep(dttime)
    return 1


if __name__ == '__main__':
    mailname_pre = 'just'
    domain = '@loveyxx.com'
    mailpasswd = 'Lslq9527'
    sn = 571
    proxy = "socks://127.0.0.1:1081"
    mailname = mailname_pre + str(sn).zfill(4) + domain
    mailname = 'xmxqb_3004@nbsky55.com'
    mailpasswd = 'Xmx&qb3'
    mailname = 'nbzr0004@yandex.com'
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
    # print (body['answer3'])
    create_cloudid(mailname, mailpasswd, body, proxy)
