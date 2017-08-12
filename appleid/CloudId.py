#coding=utf-8
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

username="xmxqb_584@nbsky55.com"
print(username)
driver=webdriver.Chrome()
driver.get("https://www.icloud.com/")
print(driver.current_window_handle)
print(driver.title)
#sleep(10)
create_element=WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"现在创建一个。")))
create_element.click()
#driver.find_element_by_link_text("现在创建一个。").click()

#sleep(5)
#switch to frame
switch_frame=WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='dialog']/div[3]/div/iframe")))
driver.switch_to.frame(switch_frame)
#driver.switch_to.frame(driver.find_element_by_xpath("//div[@role='dialog']/div[3]/div/iframe"))

WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.XPATH,"//security-answer[@answer-number='3']/div/input")))
#name
driver.find_element_by_xpath("//last-name-input/div/input").send_keys("Zrcredit")
driver.find_element_by_xpath("//first-name-input/div/input").send_keys(u"贷")

#china select

country_select=Select(driver.find_element_by_id('countryOptions'))
country_select.select_by_value('CHN')

#birthday

driver.find_element_by_xpath("//idms-error-wrapper/div/input").send_keys("19891212")

#email

driver.find_element_by_xpath("//idms-error-wrapper/div/div/input").send_keys(username)

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


#image identification

sleep(20)



#driver.find_element_by_xpath("//div[@class='button-group flow-controls pull-right']/button").click()
#继续
driver.find_element_by_xpath("//idms-toolbar/div/div/button").click()
#发送邮件中。。。。
sleep(30)
token=get_mail.get_mail(username)
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
#同意条款1
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]/label")))
print("同意1")
#WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"同意")))
sleep(5)
driver.find_element_by_xpath("//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]").click()
try:
    driver.find_element_by_xpath("//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]").click()
    print("b")
except:
    print("b nok")
try:
    driver.find_element_by_xpath("//html/body/div[@role='dialog']/div[3]/div/div[3]/div[2]/label").click()
    print("a")
except:
    print("a nok")
try:
    driver.find_element_by_link_text("同意").parent.click()
except:
    print("c nok")
sleep(60)
print(1)
#同意条款2
tongyi2=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alertdialog']/div/div/div[2]")))
tongyi2.click()
print("同意条款2成功")
sleep(5)
#开始使用iCloud
startuse=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='main']/div[2]/label")))
startuse.click()
print("点击开始使用iCloud成功")
sleep(30)
#选择 设置与注销
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@title='iCloud 设置与注销']"))).click()
#注销
WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"注销"))).click()

sleep(10)
driver.close()
driver.quit()
