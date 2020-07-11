#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 23:41
# @Author  : tanya
# @File    : main.py
# @Software: PyCharm
import os

from pythoncode.homework.po.base_page import BasePage
from pythoncode.homework.po.wework.contact import Contact
from pythoncode.my_utils import get_path


class Main(BasePage):
    def goto_contact(self):
        self.steps(os.path.join(get_path.get_root_Path(),"homework","my_yaml","steps","wework","goto_contact_steps.yml"))
        return Contact(self._driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass

    def goto_my(self):
        pass