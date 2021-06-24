# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group
from application import Application


class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    
    def test_create_group(self):
        self.app.login(user_name="admin", user_pass="secret")
        self.app.fill_group_form(Group(group_name="group_name_001", group_header="group_header_001", group_footer="group_footer_001"))
        self.app.logout()


    def test_create_empty_group(self):
        self.app.login(user_name="admin", user_pass="secret")
        self.app.fill_group_form(Group(group_name="", group_header="", group_footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
