#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 22:13
# @Author  : tanya
# @File    : test.py
# @Software: PyCharm
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desire_caps={}
desire_caps["dontStopAppOnReset"]="true"#是否重新启动app
desire_caps["skipDeviceInitialization"]="true"
desire_caps["noReset"]="true"
desire_caps["unicodeKeyBoard"]="true"
desire_caps["resetKeyBoard"]="true"
desire_caps["platformName"]="Android"
desire_caps["platformVersion"]="6.0"
desire_caps["deviceName"]="192.168.54.103:5555"
desire_caps["appPackage"]="io.appium.android.apis"
desire_caps["appActivity"]="io.appium.android.apis.ApiDemos"
driver=webdriver.Remote("http://localhost:4723/wd/hub",desire_caps)
driver.find_element_by_xpath('//*[@text="Views"]').click()
time.sleep(1)
# TouchAction(driver).press(x=528,y=1594).wait(1000).move_to(x=528,y=500).wait(1000)\
#     .press(x=528,y=1594).wait(1000).move_to(x=528,y=500).wait(1000).release().perform()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@text="Popup Menu"]').click()
# time.sleep(1)
driver.find_element_by_android_uiautomator(\
    'new UiScrollable(new UiSelector().scrollable(true).instance(0)).\
    scrollIntoView(new UiSelector().text("Popup Menu").instance(0));').click()
driver.find_element_by_xpath('//*[@content-desc="Make a Popup!"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@text="Search"]').click()
pop = driver.find_element_by_xpath('//*[@class="android.widget.Toast"]')
print(pop.get_attribute("text"))
# WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((MobileBy.XPATH,'//*[@class="android.widget.Toast"]')))
# driver.find_element_by_xpath('//*[@class="android.widget.Toast"]')



