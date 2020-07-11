#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 19:28
# @Author  : tanya
# @File    : contact.py
# @Software: PyCharm
import os

from pythoncode.homework.po.base_page import BasePage
from pythoncode.homework.po.wework.member_info import MemberInfo
from pythoncode.my_utils import get_path


class Contact(BasePage):
    def goto_add_member(self):
        self.steps(os.path.join(get_path.get_root_Path(), "homework", "my_yaml", "steps", "wework", "goto_add_member_steps.yml"))
        from pythoncode.homework.po.wework.add_member import AddMember
        return AddMember(self._driver)

    def find_member(self,name):
        try:
            return self.scroll_and_find(by="text",locator=name)
        except Exception as e:
            return None

    def select_member(self,name):
        self.scroll_find_and_click("text",name)
        return MemberInfo(self._driver)

