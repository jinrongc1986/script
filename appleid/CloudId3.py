#coding=utf-8
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

#一致等待某元素可见，默认超时10秒 LINK_TEXT 为XPATH 选择器
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

def get_yzm(driver,imgname):
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            imgurl = driver.find_element_by_xpath('//idms-captcha/div/img[@alt="安全提示图片"]').get_attribute('src')
            success = True
        except:
            attempts +=1
            if attempts == 3:
                return False
            driver.find_element_by_xpath('//button[@class ="button link first"]').click()
    request.urlretrieve(imgurl, imgname)
    result = lianzhong_api.main(file_name=imgname)
    print(result)
    return result

def double_check(driver,xpath,msg,method='XPATH'):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            if method=='XPATH':
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                success=True
            elif method=='LINK_TEXT':
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, xpath)))
                success=True
        except Exception as e:
            attempts += 1
            print(e)
            print(msg)
            if attempts == 3:
                return False
            #driver.close()
            #driver.quit()
        finally:
            return True

def double_click_c(driver,xpath,msg,method='XPATH'):
    attempts = 0
    success = False
    while attempts < 2 and not success:
        try:
            if method=='XPATH':
                todo=WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                sleep(1)
                todo.click()
                success=True
            elif method=='LINK_TEXT':
                todo = WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, xpath)))
                todo.click()
                success=True
        except Exception as e:
            attempts += 1
            print(e)
            print(msg)
            if attempts == 3:
                return False
            #driver.close()
            #driver.quit()
        finally:
            return True

def create_cloudid(mailname,mailpasswd,proxy=''):
    timestart=time.time()
    mailname=mailname
    mailpasswd=mailpasswd
    imgname=mailname.split('@')[0]+'.jpg'
    print("开始新一轮注册")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(mailname)
    ua=""
    while ("Chrome" not in ua):
        ua = generate_user_agent()
    #proxy = '127.0.0.1:1081'
    #proxy = '192.168.0.188:1080'
    option = webdriver.ChromeOptions()
    option.add_argument('--user-agent=%s'%ua)
    if proxy :
        option.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(chrome_options=option)
    # driver=webdriver.Firefox()
    driver.get("https://www.icloud.com/")
    #获取网页
    print(driver.current_window_handle)
    print(driver.title)
    try:
        create_element=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"现在创建一个。")))
        create_element.click()
    except:
        driver.close()
        driver.quit()
        return 4 #网络超时
    #switch to frame
    switch_frame=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='dialog']/div[3]/div/iframe")))
    driver.switch_to.frame(switch_frame)
    #driver.switch_to.frame(driver.find_element_by_xpath("//div[@role='dialog']/div[3]/div/iframe"))

    #账号信息页面
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//security-answer[@answer-number='3']/div/input")))
    sleep(1)
    #name
    driver.find_element_by_xpath("//last-name-input/div/input").send_keys("Zrcredit")
    driver.find_element_by_xpath("//first-name-input/div/input").send_keys(u"贷")
    #china select
    country_select=Select(driver.find_element_by_id('countryOptions'))
    country_select.select_by_value('CHN')
    #birthday
    sleep(1)
    driver.find_element_by_xpath("//idms-error-wrapper/div/input").send_keys("19891212")
    #email
    driver.find_element_by_xpath("//idms-error-wrapper/div/div/input").send_keys(mailname)
    #password
    driver.find_element_by_xpath("//password-input/input").send_keys("21B12a5&")
    driver.find_element_by_xpath("//confirm-password-input/div/input").send_keys("21B12a5&")
    #questions
    question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set0 ']/security-question/div/div/select"))
    question1.select_by_value('130')
    driver.find_element_by_xpath("//security-answer[@answer-number='1']/div/input").send_keys(u"第一财经")
    question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set1 ']/security-question/div/div/select"))
    question1.select_by_value('137')
    driver.find_element_by_xpath("//security-answer[@answer-number='2']/div/input").send_keys(u"万华化学")
    question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set2 ']/security-question/div/div/select"))
    question1.select_by_value('143')
    driver.find_element_by_xpath("//security-answer[@answer-number='3']/div/input").send_keys(u"三聚环保")
    # 将页面滚动条拖到底部
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    print("开始验证码自动识别")
    #验证码自动化
    lianzhong_result=get_yzm(driver,imgname)
    if not lianzhong_result:
        return 4 #图片无法加载
    val = json.loads(lianzhong_result)["data"]["val"]
    print(val)
    driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').send_keys(val)
    sleep(1)
    # 继续
    driver.find_element_by_xpath("//idms-toolbar/div/div/button").click()
    '''
    #手工验证模式
    print('第一次人工验证')
    sleep(15)
    #手工验证模式结束
    '''
    attempts = 0
    success=False
    while attempts < 3 and not success:
        try:
            WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@id='char0']")))
            success = True
            if os.path.exists(imgname):
                os.remove(imgname)
                print('删除正常验证码', imgname)
            with open("dama.txt", "a") as f:
                timenow=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                damaok=' PASS\n'
                f.write(timenow + damaok)
            print('发送邮件中。。。。等待30秒')
        except:
            #上报错误的打码
            lianzhong_id = json.loads(lianzhong_result)["data"]["id"]
            lianzhong_api.report(lianzhong_id)
            attempts += 1
            if attempts ==3:
                driver.close()
                driver.quit()
                return 2 #2表示图片验证尝试次数过多
            # if os.path.exists(imgname):
            #     os.rename(imgname, imgname.split('.')[0] + '_' + val + '.jpg')
            #     print("验证码失败")
            if os.path.exists(imgname):
                os.remove(imgname)
                print("删除无效验证码",imgname)
            with open("dama.txt", "a") as f:
                timenow=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                damanok=' FAIL '
                f.write(timenow + damanok + val +'\n')
            # 验证码自动化
            lianzhong_result = get_yzm(driver, imgname)
            if not lianzhong_result:
                return 4  # 图片无法加载
            val = json.loads(lianzhong_result)["data"]["val"]
            print(val)
            driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').send_keys(val)
            sleep(1)
            # 继续
            driver.find_element_by_xpath("//idms-toolbar/div/div/button").click()
            '''
            # 手工验证模式
            print('第%d次人工验证'%(attempts+1))
            sleep(15)
            # 手工验证模式结束
            '''
    sleep(30)
    token=get_mail.get_mail(mailname,mailpasswd)
    print(str(token)[2:-1])
    #verification
    token_new=str(token)[2:-1]
    driver.find_element_by_xpath("//input[@id='char0']").send_keys(token_new[0])
    driver.find_element_by_xpath("//input[@id='char1']").send_keys(token_new[1])
    driver.find_element_by_xpath("//input[@id='char2']").send_keys(token_new[2])
    driver.find_element_by_xpath("//input[@id='char3']").send_keys(token_new[3])
    driver.find_element_by_xpath("//input[@id='char4']").send_keys(token_new[4])
    driver.find_element_by_xpath("//input[@id='char5']").send_keys(token_new[5])
    #继续
    driver.find_element_by_xpath("//step-verify-code/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/button[1]").click()
    sleep(1)
    #服务器开始拒绝服务
    try:
        WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.XPATH,'//step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-popover/div/div/div/div')))
        print("gg...未知错误")
        driver.close()
        driver.quit()
        return 3 #3表示服务器拒绝服务
    except:
        pass
    #服务器超时
    try :
        WebDriverWait(driver, 10, 0.5).until_not(EC.visibility_of_element_located((By.XPATH, "//button[@id='send-code']")))
    except :
        driver.close()
        driver.quit()
        print("页面未跳转")
        return 4 #页面未跳转

    #同意条款1
    sleep(2)
    xpath="//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]/label"
    msg="等待同意1失败"
    double_check(driver,xpath,msg)
    msg="点击同意1失败"
    gg=double_click_c(driver,xpath,msg)
    if not gg:
        try:
            WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.XPATH,'//step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-popover/div/div/div/div')))
            print("gg...未知错误")
            driver.close()
            driver.quit()
            return 3  # 3表示服务器拒绝服务
        except:
            #return 5
            pass
    print("同意条款1成功")

    #同意条款2
    xpath="//div[@role='alertdialog']/div/div/div[2]"
    msg = "等待同意2失败"
    double_check(driver, xpath, msg)
    sleep(1)
    msg="点击同意2失败"
    gg=double_click_c(driver,xpath,msg)
    print("同意条款2成功")

    #开始使用iCloud
    xpath="//div[@role='main']/div[2]"
    msg = "等待开始使用iCloud失败"
    double_check(driver,xpath,msg)
    msg="点击开始使用iCloud失败"
    gg=double_click_c(driver,xpath,msg)
    print(gg)
    if not gg:
        return 5
    print("点击开始使用iCloud成功")

    #选择 设置与注销
    xpath="//div[@title='iCloud 设置与注销']"
    msg="等待点击设置失败"
    double_check(driver,xpath,msg)
    msg="点击设置失败"
    gg=double_click_c(driver,xpath,msg)
    if not gg:
        driver.close()
        driver.quit()
        return 6
    #注销
    xpath = "注销"
    msg = "等待注销失败"
    double_check(driver,xpath,msg,method='LINK_TEXT')
    msg = "注销失败"
    gg=double_click_c(driver,xpath, msg,method='LINK_TEXT')
    if not gg:
        driver.close()
        driver.quit()
        return 6
    print("注销成功")
    ###
    sleep(1)
    driver.close()
    driver.quit()
    timeend=time.time()
    timecost=timeend-timestart
    print(("本次耗时%.f秒")%timecost)
    return 1
if __name__=='__main__':
    mailname="xmxqb_797@nbsky55.com"
    mailpasswd="Xmx&qb3"
    a=create_cloudid(mailname,mailpasswd)
    print(a)