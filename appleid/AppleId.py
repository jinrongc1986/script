#coding=utf-8

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import sys

from time import sleep

import time

driver=webdriver.Chrome()

driver.get("https://www.icloud.com")

#change window
print(driver.current_window_handle)

print(driver.title)

create_element=WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"现在创建一个。")))

create_element.click()

#driver.find_element_by_link_text("现在创建一个。").click()

#sleep(10)

switch_frame=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@role='dialog']/div[3]/div/iframe")))

#switch to frame

#driver.switch_to.frame(switch_frame)

driver.switch_to.frame(driver.find_element_by_xpath("//div[@role='dialog']/div[3]/div/iframe"))

#name

driver.find_element_by_xpath("//last-name-input/div/input").send_keys("ye")

driver.find_element_by_xpath("//first-name-input/div/input").send_keys("hua")

#china select

country_select=Select(driver.find_element_by_id('countryOptions'))


country_select.select_by_value('CHN')

#birthday

driver.find_element_by_xpath("//idms-error-wrapper/div/input").send_keys("19970809")

#email

driver.find_element_by_xpath("//idms-error-wrapper/div/div/input").send_keys("1997080911@qq.com")

#password

driver.find_element_by_xpath("//password-input/input").send_keys("Zaqwsx19970809")

driver.find_element_by_xpath("//confirm-password-input/div/input").send_keys("Zaqwsx19970809")


#questions

question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set0 ']/security-question/div/div/select"))

question1.select_by_value('131')

driver.find_element_by_xpath("//security-answer[@answer-number='1']/div/input").send_keys("peggy")


question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set1 ']/security-question/div/div/select"))

question1.select_by_value('138')

driver.find_element_by_xpath("//security-answer[@answer-number='2']/div/input").send_keys("porsche")


question1=Select(driver.find_element_by_xpath("//div[@class='form-group qa-container qa-set2 ']/security-question/div/div/select"))

question1.select_by_value('147')

driver.find_element_by_xpath("//security-answer[@answer-number='3']/div/input").send_keys("Rocket")


#image identification

sleep(30)


driver.find_element_by_xpath("//div[@class='button-group flow-controls pull-right']/button").click()

sleep(5)
#verification

driver.find_element_by_xpath("//input[@id='char0']").send_keys('1')
driver.find_element_by_xpath("//input[@id='char1']").send_keys('2')
driver.find_element_by_xpath("//input[@id='char2']").send_keys('3')
driver.find_element_by_xpath("//input[@id='char3']").send_keys('4')
driver.find_element_by_xpath("//input[@id='char4']").send_keys('5')
driver.find_element_by_xpath("//input[@id='char5']").send_keys('6')




#driver.close()
#driver.quit()
