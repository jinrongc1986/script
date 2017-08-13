#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import sys
from time import sleep
import time
import get_mail
from urllib import request
import lianzhong_api
def create_cloudid(mailname,mailpasswd):
    timestart=time.time()
    mailname=mailname
    mailpasswd=mailpasswd
    imgname=mailname.split('@')[0]+'.jpg'
    print(mailname)
    driver=webdriver.Chrome()
    driver.get("https://www.icloud.com/")
    print(driver.current_window_handle)
    print(driver.title)
    #sleep(10)
    create_element=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"现在创建一个。")))
    create_element.click()
    #driver.find_element_by_link_text("现在创建一个。").click()

    #sleep(5)
    #switch to frame
    switch_frame=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='dialog']/div[3]/div/iframe")))
    driver.switch_to.frame(switch_frame)
    #driver.switch_to.frame(driver.find_element_by_xpath("//div[@role='dialog']/div[3]/div/iframe"))

    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//security-answer[@answer-number='3']/div/input")))
    #name
    driver.find_element_by_xpath("//last-name-input/div/input").send_keys("Zrcredit")
    driver.find_element_by_xpath("//first-name-input/div/input").send_keys(u"贷")

    #china select

    country_select=Select(driver.find_element_by_id('countryOptions'))
    country_select.select_by_value('CHN')

    #birthday

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
    print("请开始验证码，并提交")
    #验证码自动化
    #imgurl=driver.find_element_by_xpath('//idms-captcha/div/img[@alt="安全提示图片"]').get_attribute('src')
    #request.urlretrieve(imgurl,imgname)
    #result=lianzhong_api.main(file_name=imgname)
    #print(type(result))
    #val=result.split(":")[2].split(",")[0][1:-1]
    #driver.find_element_by_xpath('//captcha-input/div/input[@id="captchaInput"]').send_keys(val)
    #image identification
    sleep(30)
    #继续
    #driver.find_element_by_xpath("//idms-toolbar/div/div/button").click()

    WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@id='char0']")))
    print('发送邮件中。。。。等待30秒')
    #发送邮件中。。。。
    sleep(30)
    token=get_mail.get_mail(mailname,mailpasswd)
    print(token)
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
    try:
        WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"发生未知错误。")))
        print("gg")
        return 2
    except:
        pass
    try:
        WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(
            (By.XPATH,'//step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-popover/div/div/div/div')))
        print("gg")
        return 3
    except:
        pass
    #同意条款1
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]/label")))
    #WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"同意")))
    sleep(2)
    driver.find_element_by_xpath("//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]").click()
    print("同意1")
    sleep(1)

    #同意条款2
    tongyi2=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alertdialog']/div/div/div[2]")))
    sleep(1)
    tongyi2.click()
    print("同意条款2成功")
    sleep(1)
    #开始使用iCloud
    #startuse=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='main']/div[2]/label")))
    startuse=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='main']/div[2]")))
    sleep(2)
    startuse.click()
    print("点击开始使用iCloud成功")
    sleep(1)
    #选择 设置与注销
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@title='iCloud 设置与注销']"))).click()
    sleep(1)
    #注销
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"注销"))).click()
    sleep(2)
    driver.close()
    driver.quit()
    if os.path.exists(imgname):
        os.remove(imgname)
        print('remove:',imgname)
    timeend=time.time()
    timecost=timeend-timestart
    print(("耗时%f秒")%timecost)
    return 1
if __name__=='__main__':
    mailname="xmxqb_606@nbsky55.com"
    mailpasswd="Xmx&qb3"
    a=create_cloudid(mailname,mailpasswd)
    print(a)