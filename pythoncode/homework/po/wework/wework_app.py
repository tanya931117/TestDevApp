#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 18:33
# @Author  : tanya
# @File    : wework_app.py
# @Software: PyCharm
import os

import yaml
from appium import webdriver

from pythoncode.homework.po.base_page import BasePage
from pythoncode.homework.po.wework.main import Main
from pythoncode.my_utils import get_path


class WeWorkApp(BasePage):
    _appPackage="com.tencent.wework"
    _appActivity="com.tencent.wework.launch.LaunchSplashActivity"

    def start(self):
        if self._driver is None:
            root_path = get_path.get_root_Path()##'D:\\workspace\\pyworkspace\\TestDevApp\\pythoncode'
            config_path = os.path.join(root_path,"homework","my_yaml","config","wework_config.yml")
            with open(config_path) as f :
                config = yaml.safe_load(f)
                desire_caps = config[0]
                desire_caps["appPackage"]=self._appPackage
                desire_caps["appActivity"] = self._appActivity
                address = config[1]["address"]
            self._driver = webdriver.Remote(address,desire_caps)
        else:
            self._driver.start_activity(self._appPackage,self._appActivity)
        self._driver.implicitly_wait(10)
        return Main(self._driver)

    def close(self):
        self._driver.quit()
