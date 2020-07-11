#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 19:38
# @Author  : tanya
# @File    : edit_member.py
# @Software: PyCharm
import time

from appium.webdriver.common.mobileby import MobileBy

from pythoncode.homework.po.base_page import BasePage
from pythoncode.homework.po.wework.contact import Contact


class EditMember(BasePage):
    _name_element=(MobileBy.XPATH,'//*[@text="姓名　"]/..//android.widget.EditText')
    _account_element=(MobileBy.XPATH,'//*[@text="帐号　"]/..//android.widget.EditText')
    _alias_element = (MobileBy.XPATH, '//*[@text="别名　"]/..//android.widget.EditText')
    _sex_element = (MobileBy.XPATH, '//*[@text="性别"]/..//android.widget.ImageView')
    _female_element = (MobileBy.XPATH, '//*[@class="android.widget.ListView"]//*[@text="女"]')
    _male_element = (MobileBy.XPATH, '//*[@class="android.widget.ListView"]//*[@text="男"]')
    _phone_element = (MobileBy.XPATH, '//*[@text="手机　"]/..//android.widget.EditText')
    _tel_element = (MobileBy.XPATH, '//*[@text="座机　"]/..//android.widget.EditText')
    _email_element = (MobileBy.XPATH, '//*[@text="邮箱　"]/..//android.widget.EditText')
    _address_element = ()
    _post_element = ()
    _div_element = ()
    _save_element = (MobileBy.XPATH,'//*[@text="保存"]')
    _delete = (MobileBy.XPATH,"//*[@text='删除成员']")
    _delete_confirm = (MobileBy.XPATH, "//*[@text='确定']")

    def set_name(self,name):
        self.find_and_sendkeys(keys=name,by=self._name_element)
        return self

    def set_sex(self,sex):
        self.find_and_click(self._sex_element)
        if sex == "female":
            self.find_and_click(self._female_element)
        else:
            self.find_and_click(self._male_element)
        return self

    def set_phone(self,phone):
        self.find_and_sendkeys(keys=phone,by=self._phone_element)
        return self

    def set_email(self,email):
        return self
    def set_address(self,address):
        return self
    def set_div(self,div):
        return self
    def set_other(self):
        return self
    def set_account(self):
        return self
    def set_alias(self):
        return self
    def set_tel(self):
        return self
    def set_post(self):
        return self

    def save(self):
        self.find_and_click(self._save_element)
        from pythoncode.homework.po.wework.add_member import AddMember
        return AddMember(self._driver)

    def delete(self):
        self.find_and_click(self._delete)
        self.find_and_click(self._delete_confirm)
        return Contact(self._driver)
