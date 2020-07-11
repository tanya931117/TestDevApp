#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 19:30
# @Author  : tanya
# @File    : add_member.py
# @Software: PyCharm
import os

from pythoncode.homework.po.base_page import BasePage
from pythoncode.homework.po.wework.edit_member import EditMember
from pythoncode.my_utils import get_path


class AddMember(BasePage):
    def goto_add_manual(self):
        self.steps(os.path.join(get_path.get_root_Path(), "homework", "my_yaml", "steps", "wework",
                                "goto_add_member_manual_steps.yml"))
        return EditMember(self._driver)

    def return_contact(self):
        self.back(1)
        from pythoncode.homework.po.wework.contact import Contact
        return Contact(self._driver)
