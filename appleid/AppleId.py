#coding=utf-8

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

import requests

import os

import sys

from time import sleep

import time

driver=webdriver.Chrome()

driver.get("https://appleid.apple.com/account#!&page=create")

#name

driver.find_element_by_xpath("//last-name-input/div/input").send_keys("Zrcredit")

driver.find_element_by_xpath("//first-name-input/div/input").send_keys("贷")

#china select

country_select=Select(driver.find_element_by_id('countryOptions'))


country_select.select_by_value('CHN')

#birthday

driver.find_element_by_xpath("//idms-error-wrapper/div/input").send_keys("19891212")

#email

driver.find_element_by_xpath("//idms-error-wrapper/div/div/input").send_keys("xmxqb_545@nbsky55.com")

#password

driver.find_element_by_xpath("//password-input/input").send_keys("21B12a5&")

driver.find_element_by_xpath("//confirm-password-input/div/input").send_keys("21B12a5&")


#questions

question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set0 ']/security-question/div/div/select"))

question1.select_by_value('130')

driver.find_element_by_xpath("//security-answer[@answer-number='1']/div/input").send_keys("第一财经")


question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set1 ']/security-question/div/div/select"))

question1.select_by_value('137')

driver.find_element_by_xpath("//security-answer[@answer-number='2']/div/input").send_keys("万华化学")


question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set2 ']/security-question/div/div/select"))

question1.select_by_value('143')

driver.find_element_by_xpath("//security-answer[@answer-number='3']/div/input").send_keys("三聚环保")


#image identification

#sleep(30)


#driver.find_element_by_xpath("//div[@class='button-group flow-controls pull-right']/button").click()

#sleep(5)
#verification

#driver.find_element_by_xpath("//input[@id='char0']").send_keys('1')
#driver.find_element_by_xpath("//input[@id='char1']").send_keys('2')
#driver.find_element_by_xpath("//input[@id='char2']").send_keys('3')
#driver.find_element_by_xpath("//input[@id='char3']").send_keys('4')
#driver.find_element_by_xpath("//input[@id='char4']").send_keys('5')
#driver.find_element_by_xpath("//input[@id='char5']").send_keys('6')




#driver.close()
#driver.quit()
