# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import showapi
from urllib import request
from user_agent import generate_user_agent
import base64
import os
import pdb

def check_yzjg(driver):
    xpath="//div[contains(text(),'The characters were entered incorrectly. Please try again')]"
    msg="未发现验证码出错"
    flag=double_check(driver,xpath,msg)
    if flag:
        return False
    else:
        return True

def get_yzm(driver, imgname):
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            imgurl = driver.find_element_by_xpath("//img[@class='captcha__captcha__text']").get_attribute('src')
            print (imgurl)
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
    except Exception as e:
        print (e)
        print("下载图片失败")
        return False
    try:
        with open(imgname, 'rb') as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        imgurl = "data:image/jpeg;base64, " + data
        if os.path.exists(imgname):
            os.remove(imgname)
            print('删除验证码图片', imgname)
        result = showapi.main(imgurl)
    except Exception as e:
        print (e)
        print("获取验证码失败")
        return False
    if result == "":
        print("验证码api返回为空")
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
            sleep(2)
            if attempts == 3:
                return False
                # driver.close()
                # driver.quit()


def double_click_c(driver, xpath, msg, method='XPATH'):
    attempts = 0
    success = False
    while attempts < 4 and not success:
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
            sleep(2)
            if attempts == 4:
                return False
                # driver.close()
                # driver.quit()


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
    option = webdriver.ChromeOptions()
    option.add_argument('--user-agent=%s' % ua)
    if proxy:
        option.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(chrome_options=option)
    driver.get("https://mail.yandex.com/")

    # 获取网页
    sleep(dttime)
    xpath = "Create account"
    msg = "点击创建账号失败"
    flag = double_click_c(driver, xpath, msg, method='LINK_TEXT')
    if not flag:
        driver.close()
        driver.quit()
        return 4
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
        sleep(5)
        xpath="//div[@class='login__ok control__valid']"
        msg="username not available"
        flag = double_check(driver,xpath,msg)
        if not flag:
            try:
                xpath="//strong[contains(text(),'Username available')]"
                msg="username not available"
                flag=double_check(driver,xpath,msg)
            except:
                pass
        if not flag:
            try:
                xpath="//strong[contains(text(),'already registered')]"
                msg="未发现邮箱被注册"
                flag = double_check(driver,xpath,msg)
                if flag:
                    pdb.set_trace()
                    print("邮箱已经被注册")
                    driver.close()
                    driver.quit()
                    return 9
            except:
                pass
            pdb.set_trace()
            driver.close()
            driver.quit()
            return 5
        # password
        driver.find_element_by_xpath("//input[@id='password']").send_keys(mailpasswd)
        sleep(2)
        driver.find_element_by_xpath("//input[@id='password_confirm']").send_keys(mailpasswd)
        sleep(2)
        # 非手机认证
        xpath = "//label[contains(text(), 't have')]"
        msg = "点击非手机认证失败"
        flag=double_check(driver, xpath, msg)
        print ("haha:%s"%flag)
        flag = double_click_c(driver, xpath, msg)
        if not flag:
            print("点击非手机认证失败2次")
            try:
                sleep(5)
                flag = double_click_c(driver, xpath, msg)
            except:
                pass
        if not flag:
            print("点击非手机认证失败4次")
            try:
                sleep(5)
                xpath="//span[contains(text(), 't have')]"
                driver.find_element_by_xpath(xpath).click()
            except:
                pdb.set_trace()
                driver.close()
                driver.quit()
                return 4
        # questions
        try:
            driver.find_element_by_xpath("//span[@name='hint_question_id']").click()
            sleep(2)
            driver.find_element_by_xpath("""//a[contains(text(), "Your favorite musician's surname")]""").click()
        except Exception as e:
            print (e)
            print("选择安全问题失败")
            driver.close()
            driver.quit()
            return 4  # 网络超时
        driver.find_element_by_xpath("//input[@id='hint_answer']").send_keys(body['answer1'])
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        print("输入错误，关闭重来")
        return 4


    print("开始验证码自动识别")
    # 验证码自动化
    api_result = get_yzm(driver, imgname)
    if not api_result:
        driver.close()
        driver.quit()
        return 4
    try:
        val = api_result
    except:
        print("验证码格式返回错误")
        driver.close()
        driver.quit()
        return 4
    print(val)
    driver.find_element_by_xpath('//input[@id="answer"  and @name="answer"]').clear()
    driver.find_element_by_xpath('//input[@id="answer"  and @name="answer"]').send_keys(val)
    sleep(15)
    # 自动点击继续
    sleep(dttime)
    try:
        driver.find_element_by_xpath("//button[@type='submit']").click()
    except:
        print("已经人工点击注册？")
        pass
        pdb.set_trace()
    try:
        sleep(15)
        xpath="//fieldset"
        msg="跳转新页面失败"
        flag=double_check(driver,xpath,msg)
        if not flag:
            print("验证码不对？")
            yzm_flag=check_yzjg(driver)
            print ("yzm_flag:%s"%yzm_flag)
            pdb.set_trace()
    except:
        pass
    print("注册成功")
    ###
    sleep(10)
    driver.close()
    driver.quit()
    timeend = time.time()
    timecost = timeend - timestart
    print(("本次耗时%.f秒") % timecost)
    print("等待%d秒"%dttime)
    sleep(dttime)
    return 1


if __name__ == '__main__':
    mailname_pre = 'nbzr'
    domain = '@yandex.com'
    mailpasswd = 'Lslq9527'
    sn = 36
    proxy = "socks://192.168.0.61:1084"
    mailname = mailname_pre + str(sn).zfill(4)
    body = {'last_name': 'Mlqbll',
            'first_name': '贷',
            'answer1':'chen',
            'question1':'12'}
    create_emailid(mailname, mailpasswd, body, proxy)
