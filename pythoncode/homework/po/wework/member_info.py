#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:52
# @Author  : tanya
# @File    : member_info.py
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy

from pythoncode.homework.po.base_page import BasePage
from pythoncode.homework.po.wework.set_member import SetMember


class MemberInfo(BasePage):
    _set_info = (MobileBy.XPATH,"//*[@resource-id='android:id/content']/android.widget.RelativeLayout/\
            android.widget.RelativeLayout/android.widget.LinearLayout[2]")
    def send_message(self):
        pass

    def set_info(self):
        self.find_and_click(self._set_info)
        return SetMember(self._driver)