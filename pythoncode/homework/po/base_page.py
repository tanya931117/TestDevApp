#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 11:10
# @Author  : tanya
# @File    : base_page.py
# @Software: PyCharm
import time

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _driver=None
    _error_count=0
    _error_max=10
    _black_list=[]
    _params = {}

    def __init__(self,driver:WebDriver=None):
        if driver is not None:
            self._driver=driver

    def find(self,by,locator=None)->WebElement:
        try:
            element = WebDriverWait(self._driver, 5).until(lambda x: x.find_element(*by)) \
                if isinstance(by, tuple) else WebDriverWait(self._driver, 5).until(lambda x: x.find_element(by,locator))
            # element = self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            self._error_count=0
            return element
        except Exception as e:
            self._error_count+=1
            if self._error_count>=self._error_max:
                raise e
            for black in self._black_list:
                element = self._driver.find_elements(*black)
                if len(element)>0:
                    element[0].click()
                    return self.find(*by) if isinstance(by,tuple) else self.find(by,locator)
            raise e

    def scroll_and_find(self,by,locator=None):
        try:
            if locator is None:
                UiSelector = f'new UiSelector().{by[0]}("{by[1]}")'
            else:
                UiSelector = f'new UiSelector().{by}("{locator}")'
            element = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView({UiSelector}.instance(0));')
            self._error_count=0
            return element
        except Exception as e:
            self._error_count+=1
            if self._error_count>=self._error_max:
                raise e
            for black in self._black_list:
                element = self._driver.find_elements(*black)
                if len(element)>0:
                    element[0].click()
                    return self.find(by,locator)
            raise e

    def scroll_find_and_click(self,by,locator=None):
        self.scroll_and_find(by,locator).click()

    def find_and_click(self,by,locator=None):
        self.find(by,locator).click()

    def find_and_sendkeys(self,keys,by,locator=None):
        self.find(by, locator).send_keys(keys)

    def back(self,num):
        for i in range(num):
            self._driver.back()

    def find_toast(self):
        toast:WebElement = WebDriverWait(self._driver,5).\
            until(lambda x: x.find_element_by_xpath('//*[@class="android.widget.Toast"]'))
        # toast = self.find((MobileBy.XPATH,'//*[@class="android.widget.Toast"]'))
        return toast.get_attribute("text")


    def steps(self,file):
        with open(file,encoding="utf-8") as f:
            steps:list[dict] = yaml.safe_load(f)
            for step in steps:
                if ("by" in step.keys()) and ("locator" in step.keys()):
                    if ("scroll" in step.keys()) and (step["scroll"]):
                        element = self.scroll_and_find(step["by"], step["locator"])
                    else:
                        element = self.find(step["by"],step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "click":
                        element.click()
                    if action == "send" and ("params" in step.keys()):
                        for param in self._params:
                            content = step["params"].replace("{%s}"%param,self._params[param])
                        element.send_keys(content)

