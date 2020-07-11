#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 23:39
# @Author  : tanya
# @File    : test_add_member.py
# @Software: PyCharm
import os

import pytest
import yaml

from pythoncode.homework.po.wework.add_member import AddMember
from pythoncode.homework.po.wework.wework_app import WeWorkApp
from pythoncode.my_utils import get_path


def load_params():
    root_path = get_path.get_root_Path()
    with open(os.path.join(root_path, "homework", "my_yaml", "case", "add_member_case.yml")) as f:
        params = yaml.safe_load(f)
    return params

class TestAddMember():

    def setup_class(self):
        self.app = WeWorkApp()
        self.main = self.app.start()

    def teardown_class(self):
        self.app.close()

    def setup(self):
        pass

    def teardown(self):
        self.app.back(1)

    @pytest.mark.parametrize("name,phone,sex",load_params())
    def test_add_member(self,name,phone,sex):
        add_mem_page:AddMember = self.main.goto_contact().goto_add_member().goto_add_manual()\
            .set_name(name).set_phone(phone).set_sex(sex).save()
        text = add_mem_page.find_toast()
        assert text=="添加成功"
