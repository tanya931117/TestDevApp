#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 18:05
# @Author  : tanya
# @File    : set_member.py
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy

from pythoncode.homework.po.base_page import BasePage



class SetMember(BasePage):
    _goto_edit_member = (MobileBy.XPATH,"//*[@text='编辑成员']")
    def goto_edit_member(self):
        self.find_and_click(self._goto_edit_member)
        from pythoncode.homework.po.wework.edit_member import EditMember
        return EditMember(self._driver)