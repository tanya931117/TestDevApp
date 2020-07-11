#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:44
# @Author  : tanya
# @File    : test_del_member.py
# @Software: PyCharm
import os

import pytest
import yaml

from pythoncode.homework.po.wework.contact import Contact
from pythoncode.homework.po.wework.wework_app import WeWorkApp
from pythoncode.my_utils import get_path


def load_params():
    root_path = get_path.get_root_Path()
    with open(os.path.join(root_path, "homework", "my_yaml", "case", "delete_member_case.yml")) as f:
        params = yaml.safe_load(f)
    return params
class TestDelMember():
    def setup_class(self):
        self.app = WeWorkApp()
        self.main = self.app.start()

    def teardown_class(self):
        self.app.close()

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize("name",load_params())
    def test_del_member(self,name):
        contact_page:Contact = self.main.goto_contact().select_member(name).set_info().goto_edit_member().delete()
        member = contact_page.find_member(name)
        assert member is None